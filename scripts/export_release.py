#!/usr/bin/env python3
"""Export the reviewed study materials without repository history or caches."""

from pathlib import Path
import subprocess
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def main():
    subprocess.run([sys.executable, str(ROOT / "scripts/check_materials.py")], check=True)
    output = ROOT / "dist/basicrl-study.zip"
    output.parent.mkdir(exist_ok=True)
    # An allowlist prevents local notes, backups, and environment files entering a release.
    paths = [ROOT / "README.md", ROOT / "README.zh-CN.md", ROOT / ".gitignore"]
    paths.extend(ROOT / name for name in ["LICENSE", "LICENSE.md", "NOTICE"]
                 if (ROOT / name).is_file())
    for directory in ["assignments", "docs", "latex", "requirements", "scripts"]:
        paths.extend(p for p in (ROOT / directory).rglob("*") if p.is_file()
                     and not any(x.startswith(".") or x == "__pycache__"
                                 for x in p.relative_to(ROOT / directory).parts))
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(set(paths)):
            # Generated checkpoints, media, and compiler products are not release sources.
            if path.suffix in {".pth", ".mp4", ".gif", ".aux", ".log", ".out", ".pyc"}:
                continue
            if path.suffix == ".pt" and path.relative_to(ROOT).as_posix() != \
                    "assignments/01-imitation-learning/assets/expert.pt":
                continue
            name = (Path("basicrl-study") / path.relative_to(ROOT)).as_posix()
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    print(output)


if __name__ == "__main__":
    main()
