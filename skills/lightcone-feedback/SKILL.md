---
name: lightcone-feedback
description: Turn Lightcone Research feedback, bug reports, and feature requests into concise, actionable GitHub issues in the appropriate repository.
license: BSD-3-Clause
---

# Lightcone feedback

Give maintainers enough evidence to investigate without another exchange. Start
with the current session; ask only about essential gaps before filing.

## Gather the useful evidence

Capture the goal, exact action, expected versus actual behavior, and impact.
Distinguish observations from suspected causes. For bugs, include supported steps,
frequency if known, and whether independently reproduced; never present proposed
steps as tested.

Use existing session evidence and small local excerpts appropriate to the report:

- **CLI/API:** sanitized command/call and relevant error. Include the minimal safe
  config, script, or input it needs, or describe unavailable/private dependencies
  and how they prevent reproduction. A command alone may not reproduce a failure.
- **UI:** page, actions, visible result, and relevant browser details. Include an
  available screenshot or console error only when useful.
- **Agent/plugin:** invocation, relevant tool/hook error, and agent/plugin versions.
- **Docs:** page URL, problematic instruction, and expected behavior.
- **Feature/general feedback:** use case, friction, desired outcome, and workaround;
  no compulsory errors, versions, or reproduction sections.

Record relevant product/OS/runtime versions from the **failing environment**,
including local, remote/HPC, or Jupyter context. Prefer existing logs, installed
metadata, or known read-only version commands. Label lockfile versions as intended
state; laptop versions do not establish remote versions. Do not install tools,
change projects, or run costly reproductions to collect evidence.

If earlier actions or logs are missing from the visible/compacted session, treat
that context as unknown. Ask one focused, grouped question only if a maintainer
cannot otherwise take a useful next step. Mark important unavailable evidence
explicitly; accept an honest best-effort report when the tester cannot supply it.

Sanitize credentials, signed URLs, personal path prefixes, and private research
from text and images. Preserve useful relative paths and error structure. Avoid
full transcripts, environment dumps, and datasets. If essential evidence or a
security report needs privacy, use a verified private channel when available;
otherwise provide a sanitized draft and explain the limitation.

## Choose the repository and check duplicates

Read [the repository map](references/repositories.md). Default to the product the
tester used; choose a dependency repository only when existing evidence identifies
it. Use `LightconeResearch/feedback` for unclear/cross-stack feedback or this skill.
Respect an explicit destination; do not ask testers to diagnose ownership.

With available GitHub access, check authentication without exposing credentials,
then verify the destination's canonical name, visibility, and issue availability.
Search open and closed issues for distinctive symptoms and read plausible matches.
A failed search means “duplicates not checked.” For a duplicate, link it and propose
an approved comment only when there is useful new evidence. If access or the
destination is unavailable, provide a copyable draft and verified issue-page link
when possible; do not silently switch repositories.

## Review and submit once

Keep the main report short: summary/impact, steps/result, and relevant environment.
Omit empty sections; feature requests often need only a summary and example. Put
longer sanitized diagnostics in an optional `<details>` section.

Show the destination, visibility, title, and **complete sanitized body**, including
collapsed diagnostics. Obtain approval for the destination and exact content unless
already approved; material changes require revised approval. Honor draft-only
requests. Before seeking fresh approval or retrying an uncertain earlier submission,
check whether its issue/comment already exists. Stop with the draft if uncertain.

Use a structured GitHub tool or save the approved Markdown verbatim to a temporary
UTF-8 file and use `gh issue create --repo OWNER/REPO --title 'Approved title'
--body-file /path/to/issue.md`. Use `--body-file` for comments too. Safely quote
arguments; never interpolate report contents into shell code.

Apply the existing `feedback` label when permitted; never create labels or block
filing on label permissions. Verify the issue's actual labels: GitHub may silently
omit them. If missing, preserve the issue and say a maintainer must label it; never
recreate it. Check uncertain submissions before retrying. Preserve the draft on
failure, return a verified URL on success, and remove only this submission's
temporary files.
