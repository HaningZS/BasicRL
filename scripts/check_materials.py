#!/usr/bin/env python3
"""Check study-material structure, syntax, links, and identifying remnants."""

import ast
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "course number": re.compile(
        r"\b(?:CS|CSE|COMP|EE|ECE|MATH|STAT|ME|PHYS|CHEM)[ _-]*\d{3,5}[A-Z]?\b",
        re.I,
    ),
    "administrative text": re.compile(
        r"\b(?:due[ _-]*date|late[ _-]*deadline|submission[ _-]*deadline|office[ _-]*hours)\b",
        re.I,
    ),
    "school address": re.compile(
        r"https?://[^\s/\"']+\.(?:edu(?:\.[a-z]{2})?|ac\.[a-z]{2})(?:[/\s]|$)",
        re.I,
    ),
    "personal identifier": re.compile(
        r"\b(?:student(?:[ _-]+id)?|netid|学号)\s*[:=]\s*[A-Za-z0-9_-]+\b",
        re.I,
    ),
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "personal local path": re.compile(r"/(?:Users|home)/[A-Za-z][^\s\"']*"),
}
IGNORED = {".git", ".venv", ".build", "dist", "__pycache__", ".ipynb_checkpoints"}
TEXT_SUFFIXES = {".md", ".tex", ".py", ".txt", ".json", ".ipynb", ".yml", ".yaml"}


def public_files():
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT)
        if path.is_file() and not any(part in IGNORED for part in rel.parts):
            yield path


def check():
    errors = []
    topics = sorted(p for p in (ROOT / "assignments").iterdir() if p.is_dir())
    if len(topics) != 6:
        errors.append(f"Expected six topics, found {len(topics)}")
    for topic in topics:
        for name in ["README.md", "exercises/notebook.ipynb", "solutions/notebook.ipynb",
                     "solutions/solutions.tex", "solutions/solutions.pdf"]:
            if not (topic / name).is_file():
                errors.append(f"Missing {topic.name}/{name}")
    pdf_count = notebook_count = 0
    for path in public_files():
        rel = path.relative_to(ROOT)
        text = ""
        if path.suffix in TEXT_SUFFIXES or path.name in {".gitignore", "LICENSE", "NOTICE"}:
            text = path.read_text()
        elif path.suffix == ".pdf":
            pdf_count += 1
            if not shutil.which("pdftotext"):
                errors.append("pdftotext is required to inspect PDF contents")
                continue
            result = subprocess.run(["pdftotext", "-layout", str(path), "-"],
                                    capture_output=True, text=True, check=True)
            text = result.stdout
            if len(text.strip()) < 500:
                errors.append(f"PDF has too little extractable text: {rel}")
        for name, pattern in PATTERNS.items():
            if pattern.search(str(rel)) or pattern.search(text):
                errors.append(f"Identifying remnant ({name}): {rel}")
        if path.suffix == ".py":
            try:
                ast.parse(text, filename=str(rel))
            except SyntaxError as exc:
                errors.append(f"Invalid Python: {rel}: {exc}")
        if path.suffix == ".ipynb":
            notebook_count += 1
            nb = json.loads(text)
            try:
                import nbformat
                nbformat.validate(nb)
            except ImportError:
                pass
            except Exception as exc:
                errors.append(f"Invalid notebook schema: {rel}: {exc}")
            for i, cell in enumerate(nb["cells"]):
                if cell.get("outputs") or cell.get("execution_count") is not None:
                    errors.append(f"Saved notebook output or execution count: {rel}, cell {i}")
                if cell["cell_type"] == "code":
                    source = "".join(cell["source"])
                    # Setup cells contain line magics; the rest is ordinary Python.
                    source = "\n".join("pass" if line.lstrip().startswith(("%", "!"))
                                       else line for line in source.splitlines())
                    try:
                        ast.parse(source)
                    except SyntaxError as exc:
                        errors.append(f"Invalid notebook code: {rel}, cell {i}: {exc}")
            if set(nb["metadata"]) - {"kernelspec", "language_info"}:
                errors.append(f"Unexpected notebook runtime metadata: {rel}")
        if path.suffix == ".md":
            for target in re.findall(r"\]\(([^\s)]+)\)", text):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                target = unquote(target.split("#", 1)[0])
                if target and not (path.parent / target).exists():
                    errors.append(f"Broken local link: {rel}: {target}")
    if pdf_count != 6 or notebook_count != 12:
        errors.append(f"Expected 6 PDFs and 12 notebooks, found {pdf_count} and {notebook_count}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Passed: {len(topics)} topics, {notebook_count} notebooks, {pdf_count} PDFs; "
          "structure, Python syntax, local Markdown links, text scan, and notebook hygiene.")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())
