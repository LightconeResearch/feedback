---
name: lightcone-feedback
description: Draft and file Lightcone Research beta feedback, bug reports, and feature requests in the appropriate GitHub repository using the current session as evidence.
license: BSD-3-Clause
---

# Lightcone feedback

Turn the user's feedback into a useful GitHub issue with minimal interruption.
Use the current session; ask only for missing information that changes the report.
This skill works in Claude Code and Codex, using ordinary conversation and `gh`.

## Understand and route

Use the user's description and relevant session evidence to identify the observed
behavior and expected outcome. Feature requests need the use case and desired
behavior, not a fabricated error or reproduction.

Read [the repository map](references/repositories.md) before choosing a target.
Route by the component supported by the evidence, not just the app where an error
appeared. Explain the selected repository in one sentence. Respect a user-specified
destination; flag an apparent mismatch without silently changing it.

Do not turn reporting into a debugging project. Read small relevant excerpts if
needed, but do not change the project, install or upgrade packages, rerun expensive
analyses, or submit compute jobs just to gather a report.

## Gather evidence

- Keep the command or user action, expected and actual behavior, a short error
  excerpt, and reproduction steps already supported by the session. Distinguish
  observations from suspected causes; do not claim untested steps reproduce it.
- Record relevant installed versions and the environment that actually failed:
  agent, CLI or package, Python/Node, OS, and local versus remote/HPC. Use existing
  logs, package metadata, lockfiles, or a known version command. A laptop's version
  is not evidence about a remote cluster or a separate Jupyter environment.
- For plugin problems include the plugin version, agent name, invocation, and hook
  error when available. For docs include the page URL and problematic instruction.
- Unknown versions are fine. Do not fetch a new `uvx` tool to discover the version
  of a different executable that ran earlier.
- Include only what maintainers need. Redact credentials, tokens, signed URLs,
  personal path prefixes, and private research data. Keep useful relative paths.
  Never upload full session transcripts, environment dumps, or datasets by default.

## Check the destination and duplicates

If `gh` is available, check authentication without displaying credentials. Verify
the target's canonical name, visibility, and whether issues are enabled:

```sh
gh repo view LightconeResearch/REPO --json nameWithOwner,url,isPrivate,hasIssuesEnabled
```

Follow a verified rename; do not assume the historical name `ASTRA` is the format
repository. If access or authentication is unavailable, still finish a copyable
draft and give a verified issue-page link where possible. An inaccessible private
repository is not a reason to publish its details in a different public repo.

Search a few distinctive terms in the chosen repo before creating an issue:

```sh
gh issue list --repo LightconeResearch/REPO --state all --search 'distinctive terms' --limit 10 --json number,title,url,state
```

Read a plausible match before calling it a duplicate. If it is the same issue,
show its link and offer any useful new evidence as a comment draft. Do not create
another issue or post a comment without the user's authorization for that action.
A failed search means duplicates were not checked, not that none exist.

## Review the report

Show the repository link and visibility, a specific title, and the complete body.
Use only applicable sections:

```markdown
## What happened
[Observed behavior and expected outcome, or feature request and use case.]

## Reproduction
[Minimal steps supported by the session; state if not independently reproduced.]

## Error
[Short redacted excerpt, if any.]

## Environment
[Relevant versions, agent, OS and execution environment; unknown where necessary.]
```

Mention another component only when it helps triage; avoid speculative blame.
Ask for approval of this destination and exact content before posting, unless
the user has already approved both. An ordinary conversational reply is sufficient;
do not require a harness-specific question tool. Honor draft-only requests.
If editing changes the destination or materially changes the report, obtain approval
for the revised version.

## File once

Use a structured GitHub tool if available, or write the approved Markdown verbatim
to a temporary UTF-8 file outside the project and pass it to `gh`:

```sh
gh issue create --repo LightconeResearch/REPO --title 'Approved title' --body-file /path/to/temporary/issue.md
```

The paths and text above are placeholders. Use safely quoted arguments, not shell
interpolation of the report. Use `--body-file` for an approved comment as well.
Apply `beta-feedback` only if the label exists and the account can apply it; creating
a report must not depend on label-management permissions. Do not create labels.

If submission times out or its outcome is uncertain, look for the newly created
issue before retrying. Never blindly repeat an issue/comment mutation. On a definite
failure preserve the draft and explain the blocker. Return the issue or comment URL
only after verifying success, and remove only the temporary file you created.
