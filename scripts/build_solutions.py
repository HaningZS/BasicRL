#!/usr/bin/env python3
"""Compile every solution and keep TeX intermediates outside the materials."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", help="Build one topic directory instead of all six")
    parser.add_argument("--offline", action="store_true", help="Use only locally cached Tectonic resources")
    parser.add_argument("--bundle", help="Optional local Tectonic resource bundle")
    args = parser.parse_args()
    sources = sorted((ROOT / "assignments").glob("*/solutions/solutions.tex"))
    if args.topic:
        sources = [p for p in sources if p.parent.parent.name == args.topic]
    if not sources:
        parser.error("No matching solution sources")
    tectonic = shutil.which("tectonic")
    latexmk = shutil.which("latexmk")
    if not tectonic and not latexmk:
        parser.error("Install Tectonic or a TeX distribution containing latexmk")
    for source in sources:
        topic = source.parent.parent.name
        output = ROOT / ".build" / "pdf" / topic
        output.mkdir(parents=True, exist_ok=True)
        if tectonic:
            command = [tectonic, "--untrusted", "--keep-logs", "--outdir", str(output), source.name]
            if args.offline:
                command.insert(1, "--only-cached")
            if args.bundle:
                command[1:1] = ["--bundle", str(Path(args.bundle).resolve())]
        else:
            command = [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                       "-no-shell-escape", f"-outdir={output}", source.name]
        print(f"Building {topic}", flush=True)
        # Reproducible PDF timestamps rather than personal authoring metadata.
        env = dict(os.environ, SOURCE_DATE_EPOCH="0")
        subprocess.run(command, cwd=source.parent, env=env, check=True)
        pdf = output / "solutions.pdf"
        if not pdf.is_file() or pdf.stat().st_size == 0:
            raise RuntimeError(f"Compiler produced no PDF: {topic}")
        shutil.copy2(pdf, source.with_suffix(".pdf"))
    print(f"Compiled {len(sources)} solution PDFs.")


if __name__ == "__main__":
    main()
