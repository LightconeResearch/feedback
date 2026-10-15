# Lightcone feedback

Report Lightcone bugs and suggestions from your agent session. The skill drafts an issue for your approval, then routes it to the appropriate Lightcone repository and applies a `feedback` label when permitted.

## Install as a plugin

**Claude Code**

```sh
claude plugin marketplace add LightconeResearch/feedback
claude plugin install lightcone-feedback@lightcone-feedback
```

**Codex**

```sh
codex plugin marketplace add LightconeResearch/feedback
codex plugin add lightcone-feedback@lightcone-feedback
```

## Install from this repo

Requires Git and Python 3:

```sh
git clone https://github.com/LightconeResearch/feedback.git
cd feedback
python3 scripts/install.py --agent both
```

Use `--agent claude` or `--agent codex` to install for just one.

## Use

Install the [GitHub CLI (`gh`)](https://cli.github.com/) where your agent runs and sign in with `gh auth login` so it can submit issues directly. No repo clone is needed for submission.

Start a new agent session and ask: **“Use Lightcone Feedback to report this: …”**
