#!/usr/bin/env python3
"""Bundle the canonical skill into the marketplace plugin, or check for drift."""

import argparse
from pathlib import Path
import shutil


def files(root):
    return {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the packaged skill differs")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    source = repo / "skills" / "lightcone-feedback"
    target = repo / "plugins" / "lightcone-feedback" / "skills" / "lightcone-feedback"
    if not (source / "SKILL.md").is_file():
        parser.error(f"Missing canonical skill: {source}")
    if args.check:
        if files(source) != files(target):
            parser.error("Packaged skill is out of date. Run python3 scripts/build_plugin.py")
        print("Packaged skill matches the canonical source.")
    else:
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)
        print(f"Built {target}")


if __name__ == "__main__":
    main()
