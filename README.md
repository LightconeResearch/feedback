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

## License

BSD 3-Clause. See [LICENSE](LICENSE).
