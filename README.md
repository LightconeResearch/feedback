# Lightcone feedback

Report Lightcone bugs, confusing workflows, documentation problems, and feature
requests from the conversation where they happened. The skill collects relevant
context, asks about essential gaps, and shows you a concise report before posting
to our [shared beta feedback inbox](https://github.com/LightconeResearch/feedback-skill/issues).

**You do not need to clone this repository to install the plugin or submit feedback.**
Choose one installation method below. You can also
[open an issue in your browser](https://github.com/LightconeResearch/feedback-skill/issues/new)
without installing anything.

## Install through your agent's plugin marketplace

The commands below run in a terminal. Your agent downloads and installs the plugin;
you do not need to manage a checkout or copy files yourself.

### Claude Code

```sh
claude plugin marketplace add LightconeResearch/feedback-skill
claude plugin install lightcone-feedback@lightcone-feedback
```

Start a new session in the project where the problem happened, then use:

```text
/lightcone-feedback:lightcone-feedback The run finished, but Lab still shows the old plot.
```

### Codex

```sh
codex plugin marketplace add LightconeResearch/feedback-skill
codex plugin add lightcone-feedback@lightcone-feedback
```

Start a new task in your project, then select the installed skill or use:

```text
$lightcone-feedback:lightcone-feedback The run finished, but Lab still shows the old plot.
```

If your Codex version has no `plugin` command, use the direct skill download below.
In either agent, you can also ask naturally: “Use Lightcone Feedback to report this.”

This repository provides a **custom marketplace** named `lightcone-feedback`.
It is separate from the existing `lightcone-research` marketplace and is not an
official Anthropic or OpenAI directory listing. The install ID uses the form
`plugin-name@marketplace-name`, which is why the name appears twice.
See the official [Claude marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces)
and [Codex marketplace commands](https://learn.chatgpt.com/docs/developer-commands#codex-plugin-marketplace).

## Download just the skill

No Git or Python is needed for this option:

1. [Download the skill ZIP](https://github.com/LightconeResearch/feedback-skill/releases/latest/download/lightcone-feedback-skill.zip).
2. Unzip it to get a folder named `lightcone-feedback` containing `SKILL.md` and `LICENSE`.
3. Put that folder in your agent's skills directory (create the directory if needed):

   | Agent | Personal installation | Project installation |
   | --- | --- | --- |
   | Claude Code | `~/.claude/skills/lightcone-feedback/` | `.claude/skills/lightcone-feedback/` |
   | Codex | `~/.agents/skills/lightcone-feedback/` | `.agents/skills/lightcone-feedback/` |

   `~` means your user home directory. Project paths are relative to your project.
   Check that `SKILL.md` is directly inside `lightcone-feedback`, not nested in a second copy of the folder.
4. Start a new session. Invoke `/lightcone-feedback` in Claude Code or
   `$lightcone-feedback` in Codex. Direct installs have no plugin namespace.

These locations follow the official [Claude skills documentation](https://code.claude.com/docs/en/skills)
and [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills).

### Optional: install from the source repository

If you prefer a checkout:

```sh
git clone https://github.com/LightconeResearch/feedback-skill.git
cd feedback-skill
python3 scripts/install.py --agent both
```

Or [download the source ZIP](https://github.com/LightconeResearch/feedback-skill/archive/refs/heads/main.zip),
extract it, open a terminal in `feedback-skill-main`, and run the same Python command.
Use `--agent claude` or `--agent codex` for only one agent. To install in an existing
project, add `--project /path/to/your/project`. The installer copies the skill and
refuses to overwrite an existing installation. You can delete the download afterward.

## Submit feedback directly to GitHub

Install the [GitHub CLI](https://cli.github.com/) and sign in once, on the machine
where your agent runs:

```sh
gh auth login
```

If your agent runs on a cluster or in a remote Jupyter environment, authenticate
there. Alternatively, the skill can use an available authenticated GitHub tool.

After you describe the problem, the skill checks for duplicates, prepares the
report, and asks you to approve its exact contents. It then creates the issue
directly through GitHub, using a command like:

```sh
gh issue create --repo LightconeResearch/feedback-skill \
  --title 'Approved issue title' --body-file /path/to/report.md
```

The agent prepares that temporary report file for you. This is an **issue submission**,
not a Git push: no clone, fork, commit, or repository code-write access is needed.
It uses your GitHub account, so the issue is attributed to you. Without GitHub
access, the skill still gives you a copyable draft for the browser issue form.
See [`gh issue create`](https://cli.github.com/manual/gh_issue_create).

Reports are public. Review the draft before approving it. The skill excludes
credentials and private research data, avoids uploading full transcripts, and
does not rerun expensive jobs to collect diagnostics. A private support channel
must be established separately before sensitive evidence can be shared.

## Updates and removal

For marketplace installs, use your agent's plugin management to update or remove
`lightcone-feedback`. For direct installs, move the old skill folder outside the
`skills` directory before replacing it with a fresh download; delete the installed
folder to uninstall. Choose either a plugin install or a direct skill install to
avoid seeing duplicate skills.

## Maintainers

All beta feedback lands in this repo. Use the [component map](docs/triage.md) to
identify implementation owners and link implementation work back to the original
report. Testers do not need to choose a component repository.

Edit [the canonical skill](skills/lightcone-feedback/SKILL.md), then rebuild the
copy packaged for marketplace installation:

```sh
python3 scripts/build_plugin.py
python3 scripts/build_plugin.py --check
```

The plugin lives in `plugins/lightcone-feedback/`, with manifests for both agents.
Do not edit its generated skill copy directly. The scripts use Python's standard
library. A plugin ZIP is also attached to each release for distribution or review.

To appear in an official directory, submit separately for review; hosting this
custom marketplace does not create an official listing. See
[Anthropic's official plugin directory](https://github.com/anthropics/claude-plugins-official)
and [OpenAI's skills-only submission guide](https://developers.openai.com/plugins/guides/submit-claude-plugin).

Adapted from the archived Lightcone Research
[feedback skill](https://github.com/LightconeResearch/agent-skills/blob/4bc51922d14fcee59ced4fef034f3a7fa606cde1/skills/feedback/SKILL.md),
with one inbox and evidence-based reporting. BSD 3-Clause; see [LICENSE](LICENSE).
