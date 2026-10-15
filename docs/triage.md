# Feedback triage

The installed skill uses the [repository map](../skills/lightcone-feedback/references/repositories.md)
to file feedback in the appropriate component repository. Update that canonical
reference when ownership changes, then run `python3 scripts/build_plugin.py`.

`LightconeResearch/feedback` remains the fallback for unclear or cross-stack
feedback and issues with the reporting skill itself. Keep one issue per report;
link implementation work when it belongs elsewhere.

The mapped repositories have a `feedback` label. The reporting skill applies it
when the reporter has permission and verifies the result. Outside contributors
may need a maintainer to add the label; creating the issue does not grant label
permissions. Repository-side auto-labeling is not configured by this skill.
