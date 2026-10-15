# Lightcone feedback

Report Lightcone bugs and suggestions from your agent session. The skill drafts an issue for your approval, then posts it to our [feedback inbox](https://github.com/LightconeResearch/feedback-skill/issues).

## Install as a plugin

**Claude Code**

```sh
claude plugin marketplace add LightconeResearch/feedback-skill
claude plugin install lightcone-feedback@lightcone-feedback
```

**Codex**

```sh
codex plugin marketplace add LightconeResearch/feedback-skill
codex plugin add lightcone-feedback@lightcone-feedback
```

## Install from this repo

Requires Git and Python 3:

```sh
git clone https://github.com/LightconeResearch/feedback-skill.git
cd feedback-skill
python3 scripts/install.py --agent both
```

Use `--agent claude` or `--agent codex` to install for just one.

## Use

Install the [GitHub CLI (`gh`)](https://cli.github.com/) where your agent runs and sign in with `gh auth login` so it can submit issues directly. No repo clone is needed for submission.

Start a new agent session and ask: **“Use Lightcone Feedback to report this: …”**
