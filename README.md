# Lightcone feedback

This is where bug reports, feature requests and other feedback on the
[Lightcone Research](https://github.com/LightconeResearch) stack go: `lc`,
Lightcone Lab, ASTRA, MySTRA, the docs and the agent skills. Open an issue
here for any of them, and the maintainers will take it to the right project.

## Report from your agent

The `lightcone` plugin from
[agent-skills](https://github.com/LightconeResearch/agent-skills) includes a
`feedback` skill. Tell your agent:

```text
Report this to the Lightcone team.
```

It drafts an issue here from what happened in the session, shows it to you,
and files it once you approve. It uses the [GitHub CLI](https://cli.github.com/)
(`gh`). The [Agent Skills docs](https://docs.lightconeresearch.org/agent-skills)
explain how to install the plugin.

## Report by hand

[Open an issue](https://github.com/LightconeResearch/feedback/issues/new). Say
which part of the stack you were using, what you did, what you expected and
what happened. For a bug, add the versions and the error. Leave out
credentials, tokens and unpublished research.

## Moving from the old plugin

This repository used to ship a `lightcone-feedback` plugin. The skill now lives
in the `lightcone` plugin, so if you installed the old one, remove it. In
Claude Code:

```bash
claude plugin uninstall lightcone-feedback@lightcone-feedback
claude plugin marketplace remove lightcone-feedback
```

Remove the `lightcone-feedback` plugin and marketplace from Codex the same way.
If you installed it with this repository's old install script, delete
`~/.claude/skills/lightcone-feedback` and `~/.agents/skills/lightcone-feedback`
instead. Then install the `lightcone` plugin as the
[Agent Skills docs](https://docs.lightconeresearch.org/agent-skills/getting-started)
describe.

## License

BSD 3-Clause. See [LICENSE](LICENSE).
