# Lightcone feedback

A portable beta-feedback skill for **Claude Code and Codex**. It turns session
context into an actionable report in one shared GitHub inbox, and shows the
tester the complete report before posting. Maintainers handle component triage.

The same `skills/lightcone-feedback/` folder works in both agents. No plugin
marketplace, MCP server, or Lightcone installation is required to load the skill.

## Install

Download or clone this repository, open a terminal in its root, then run:

```sh
python3 scripts/install.py --agent both
```

Use `--agent claude` or `--agent codex` for just one. Python 3 is needed only by
the installer. It copies the self-contained skill to:

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

## One beta inbox

The configured destination is `LightconeResearch/feedback-skill`, intended to host
both this skill and all beta reports. **Publication is pending:** the repository
must exist with public issues enabled before distributing this release to testers.
If a different name is chosen, update the destination in `SKILL.md` and this README
before distribution. The skill verifies access before posting and preserves a
copyable draft if the destination is unavailable.

Testers describe the product they used; they do not choose an implementation repo.
Maintainers can use the [component map](docs/triage.md) to investigate or link
implementation work. That map is not installed with the skill.

## What a useful report contains

A maintainer should be able to take a concrete next step: reproduce a failure,
inspect a specific error, locate a UI or documentation problem, or assess a feature
request. The skill gathers existing session evidence first and asks a focused
question before filing when an essential detail is missing. It does not require
irrelevant fields or promise that every issue can be resolved without follow-up.

Reports identify the goal, expected and actual behavior, impact, supported steps,
and relevant environment. Evidence depends on the problem; longer sanitized
logs can go in a collapsible section. Unknowns and untested reproduction steps are
identified honestly. Public reports must not expose credentials or private
research data. Sensitive evidence stays out of the issue; a private support
channel must be established separately before such evidence can be shared.

## Development and provenance

Edit the canonical skill under `skills/lightcone-feedback/`. There are no generated
copies in this repository. The installer uses only Python's standard library.

Adapted from the archived Lightcone Research
[feedback skill](https://github.com/LightconeResearch/agent-skills/blob/4bc51922d14fcee59ced4fef034f3a7fa606cde1/skills/feedback/SKILL.md),
with provider-neutral interaction, a shared inbox, and a focus on actionable reports. Distributed under
the BSD 3-Clause license; see [LICENSE](LICENSE).
