# Lightcone feedback

A portable beta-feedback skill for **Claude Code and Codex**. It turns session
context into a concise GitHub report, chooses the owning Lightcone repository,
and shows the tester the destination and complete report before posting.

The same `skills/lightcone-feedback/` folder works in both agents. No plugin
marketplace, MCP server, or Lightcone installation is required to load the skill.

## Install

Download or clone this repository, open a terminal in its root, then run:

```sh
python3 scripts/install.py --agent both
```

Use `--agent claude` or `--agent codex` for just one. Python 3 is needed only by
the installer. It copies the skill and its repository map to:

- Claude Code: `~/.claude/skills/lightcone-feedback/`
- Codex: `~/.agents/skills/lightcone-feedback/`

For a project-scoped installation in an existing directory:

```sh
python3 scripts/install.py --agent both --project /path/to/your/project
```

The corresponding `.claude/skills/` and `.agents/skills/` directories can be
committed with the project. The installer refuses to overwrite an existing skill.
To update, move the previous `lightcone-feedback` directory outside the relevant
`skills/` directory, then install again. Remove the installed directory to uninstall.
Downloads and clones may be deleted after installation; the installed copies are
self-contained. Alternatively, manually copy `skills/lightcone-feedback/` into
the appropriate discovery directory above.

These locations follow the official
[Claude Code skill documentation](https://code.claude.com/docs/en/skills) and
[Codex skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Use

Start a new agent session in the project where the problem happened.

Claude Code:

```text
/lightcone-feedback The run finished, but Lab still shows the old plot.
```

Codex:

```text
$lightcone-feedback The run finished, but Lab still shows the old plot.
```

You can also ask naturally to report Lightcone beta feedback. Bugs, confusing
workflows, documentation problems, and feature requests are all supported.

To post issues using the GitHub CLI, install [gh](https://cli.github.com/) and run
`gh auth login` once. The skill can still prepare a copyable report when GitHub
access is unavailable. It does not authenticate on your behalf, modify the
research project, or run an analysis to reproduce the failure.

## Routing

The [repository map](skills/lightcone-feedback/references/repositories.md) covers
the ASTRA specification, Python tools, TypeScript SDK, CLI, Lab, shared UI,
agent skills, MySTRA, publication themes, and documentation. It explains the
boundaries and handles uncertain ownership without filing across multiple repos.

Repository names and visibility were checked on 2026-10-15 against GitHub and the
[Lightcone docs](https://docs.lightconeresearch.org/). The skill verifies the selected
destination again before filing. Keep the map current as the stack evolves.

## Development and provenance

Edit the canonical skill under `skills/lightcone-feedback/`. There are no generated
copies in this repository. The installer uses only Python's standard library.

Adapted from the archived Lightcone Research
[feedback skill](https://github.com/LightconeResearch/agent-skills/blob/4bc51922d14fcee59ced4fef034f3a7fa606cde1/skills/feedback/SKILL.md),
with provider-neutral interaction and current component routing. Distributed under
the BSD 3-Clause license; see [LICENSE](LICENSE).
