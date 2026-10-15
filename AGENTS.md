# Editing this repository

- Edit the canonical skill in `skills/lightcone-feedback/`.
- `plugins/lightcone-feedback/skills/lightcone-feedback/` is a generated copy;
  do not edit it directly.
- After changing the source, run `python3 scripts/build_plugin.py`, then
  `python3 scripts/build_plugin.py --check`. Commit the source and generated
  copy together. CI runs the check on pushes and pull requests; it does not
  rebuild or commit files for you.
- Plugin and marketplace manifests are maintained directly. For a plugin
  release, bump both plugin manifests to the same version.
- Keep the README focused on installation and basic usage.
