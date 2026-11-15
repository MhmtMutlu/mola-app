#!/usr/bin/env python3
"""Copies the legal texts from the app repository (the single source) into src/. Run after they change, then build.

    python3 tools/import_legal.py ../mola
"""
import pathlib, shutil, sys

FILES = {
    "privacy-policy.tr.md": "privacy.tr.md",
    "privacy-policy.en.md": "privacy.en.md",
    "terms-of-use.tr.md": "terms.tr.md",
    "terms-of-use.en.md": "terms.en.md",
    "kvkk-aydinlatma.tr.md": "kvkk.tr.md",
}

source = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "../mola") / "docs" / "legal"
target = pathlib.Path(__file__).resolve().parent.parent / "src"
for name, copy in FILES.items():
    if not (source / name).exists():
        raise SystemExit(f"missing: {source / name}")
    shutil.copyfile(source / name, target / copy)
    print(f"{name} → src/{copy}")
