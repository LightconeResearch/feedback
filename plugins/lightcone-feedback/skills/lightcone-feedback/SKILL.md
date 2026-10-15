---
name: lightcone-feedback
description: Turn Lightcone Research beta feedback, bug reports, and feature requests into concise, actionable issues in the shared feedback inbox.
license: BSD-3-Clause
---

# Lightcone feedback

Help a maintainer investigate without another exchange with the tester. Use the
current session first, ask only essential questions, and keep the report concise.

**Feedback inbox:** `LightconeResearch/feedback`. Send all beta feedback here;
maintainers handle component routing. Name the affected product when known, without
asking testers to diagnose dependencies. Respect an explicitly requested destination.
Verify the inbox exists and accepts issues before posting; otherwise deliver a draft.

## Build an actionable report

Extract what the tester was trying to do, their exact action, expected and actual
behavior, and practical impact. Separate observations from suspected causes.
For bugs, include the smallest supported sequence of steps, frequency if known,
and whether the failure was independently reproduced. Frequency and independent
reproduction are separate facts. Never present proposed steps as tested steps.

Collect relevant evidence already available in the session or small local excerpts:

- **CLI / API:** exact command or call with sanitized arguments, relevant error and
  nearby context, and a small non-sensitive input or input description when needed.
- **UI:** product/page, action sequence, visible result or error, and browser/version
  when relevant. Use an available screenshot or console error only if it adds useful
  evidence; do not require both or expose private page contents.
- **Agent / plugin:** Claude Code or Codex version, plugin version, invocation, and
  relevant hook/tool error when available.
- **Docs:** page URL, problematic instruction, and what the tester expected or tried.
- **Feature / general feedback:** use case, current limitation or friction, desired
  outcome, and any workaround. Do not force an error, versions, or reproduction.

Record versions and execution context relevant to the failure: affected product,
OS, runtime when relevant, and local, remote/HPC, or Jupyter environment. Prefer
existing logs, installed metadata, or a known read-only version command. A lockfile
is intended dependency state, not proof of what ran; label its source. Laptop
versions do not establish remote versions. Never fetch a new executable to discover
which version failed earlier.

Before drafting, check: can a maintainer identify the affected workflow, understand
the discrepancy, and take a useful next investigative step? If an essential fact is
missing, ask a short, grouped question before submission. For example, “Which page
were you on, what did you click, and what appeared?” Do not ask for facts already in
the session or turn optional diagnostics into a questionnaire. Mark important
unavailable evidence as unknown; if the tester cannot supply it, preserve an honest
best-effort report rather than inventing facts or indefinitely blocking feedback.

Do not turn reporting into a debugging project: no project changes, installations,
upgrades, expensive reruns, or compute jobs to gather evidence. Do not claim a cause
without evidence.

## Keep public reports safe

Include only what maintainers need. Sanitize credentials, tokens, signed URLs,
personal path prefixes, and unpublished or private research data in text and images.
Keep useful relative paths and non-sensitive error structure. Do not upload full
transcripts, environment dumps, datasets, or private attachments by default.
If essential evidence cannot safely be public, describe the limitation and use a
verified private reporting channel if available; do not invent one or publish the
sensitive details. Treat potential security reports the same way.

## Check the inbox and duplicates

If an earlier submission has an uncertain outcome, check whether its issue or
comment already exists before requesting fresh approval or preparing another post.
If the outcome cannot be established, preserve the draft and explain the uncertainty.

If GitHub access is available, check authentication without displaying credentials,
then verify the destination's canonical name, visibility, and issue availability:

```sh
gh repo view LightconeResearch/feedback --json nameWithOwner,url,isPrivate,hasIssuesEnabled
gh issue list --repo LightconeResearch/feedback --state all --search 'distinctive terms' --limit 10 --json number,title,url,state
```

Read plausible matches before calling a report a duplicate, including whether a
closed issue covers the same version/behavior. For a matching issue, show its link
and draft a comment only if there is useful new evidence. Obtain authorization for
that comment instead of silently creating a new issue. A failed search means
“duplicates not checked,” not “no duplicates.” If access, authentication, or the inbox
is unavailable, finish a copyable draft and provide a verified issue-page link when
possible. Do not install tools or switch repositories just to bypass a blocker.

## Review, then file once

Show the destination and visibility, a specific title, and the complete sanitized
body. Keep the main report short; use only sections that help this report:

```markdown
## Summary
[Goal, expected vs. actual behavior, and impact; or use case and requested outcome.]

## Steps and result
[Exact actions, observed result, frequency/reproduction status, and short error.]

## Environment
[Only relevant versions and actual execution context; label important unknowns.]
```

Put longer useful sanitized diagnostics in an optional `<details>` section with a
clear `<summary>`. Include that section in the review too. Omit empty sections and
avoid speculative blame. Feature requests often need only the summary and example.

Ask for approval of the destination and exact content before posting unless the user
already approved both. Ordinary conversation is sufficient in either agent. Honor
draft-only requests. Material edits or a destination change require revised approval.

Use a structured GitHub tool, or write the approved Markdown verbatim to a temporary
UTF-8 file and pass its path to `gh`:

```sh
gh issue create --repo LightconeResearch/feedback --title 'Approved title' --body-file /path/to/temporary/issue.md
```

Use safely quoted arguments, never shell interpolation of report contents. Use
`--body-file` for approved comments too. Apply `beta-feedback` only if the label
already exists and permissions allow; do not create labels or make filing depend on
label permissions.

If posting times out or has an uncertain result, look for the newly created issue
or comment before retrying. Never blindly repeat a mutation. If the result remains
uncertain, stop and explain; on definite failure preserve the draft. Return the
issue/comment URL only after verifying success. Remove only temporary files you
created for this submission.
