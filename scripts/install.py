#!/usr/bin/env python3
"""Copy the portable skill into Claude Code and/or Codex discovery directories."""

import argparse
from pathlib import Path
import shutil
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=("claude", "codex", "both"), default="both")
    parser.add_argument("--project", type=Path, help="Install in this existing project instead of your user directory")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "skills" / "lightcone-feedback"
    base = args.project.expanduser().resolve() if args.project else Path.home()
    if not base.is_dir():
        parser.error(f"Installation root is not a directory: {base}")
    if not (source / "SKILL.md").is_file():
        parser.error(f"Skill source is missing: {source}")
    folders = {"claude": ".claude", "codex": ".agents"}
    agents = tuple(folders) if args.agent == "both" else (args.agent,)
    targets = [base / folders[agent] / "skills" / source.name for agent in agents]
    # Check every destination before copying either one. Never overwrite a skill.
    for target in targets:
        if target.exists() or target.is_symlink():
            parser.error(f"Already exists: {target}. Move the old copy outside the skills directory before reinstalling.")
    for target in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target)
        print(f"Installed {target}")
    print("Start a new agent session to use lightcone-feedback.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
