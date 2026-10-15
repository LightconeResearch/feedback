# Lightcone repository map

Use the product where the symptom appeared unless existing evidence identifies a
specific dependency. Testers do not need to know this map or diagnose ownership.
Choose one destination, explain it briefly, and include it in the report preview.
All repos below were public with issues enabled when checked on 2026-10-15;
verify the selected destination before submission.

| Symptom or component | Repository | Boundary |
| --- | --- | --- |
| ASTRA fields, schema/model constraints, specification ambiguity, format changes | [astra-spec](https://github.com/LightconeResearch/astra-spec) | The format, not recipe execution. |
| `astra` CLI, Python validation/resolution, scaffolding, paper cache, quote/evidence checks | [astra-tools](https://github.com/LightconeResearch/astra-tools) | Python tooling; the historical `ASTRA` repo redirects here. |
| `lc` setup, execution, materialization, environments, containers, provenance, freshness, cluster jobs | [lightcone-cli](https://github.com/LightconeResearch/lightcone-cli) | Execution; a known Python validation bug belongs in astra-tools. |
| Lightcone skill instructions, plugin packaging, hooks or obsolete command guidance | [agent-skills](https://github.com/LightconeResearch/agent-skills) | Correctly invoked tools failing belong to their owners. This feedback skill itself belongs in feedback. |
| Lab Home, Jupyter integration, agent launch/chat, loading/refreshing files, artifacts or papers | [jupyterlab-lightcone](https://github.com/LightconeResearch/jupyterlab-lightcone) | Default for Lab symptoms without an isolated dependency defect. |
| `@astra-spec/sdk`, TypeScript validation/resolution, resolved data or artifact bindings | [astra-typescript](https://github.com/LightconeResearch/astra-typescript) | Use when data/resolution is demonstrably wrong. |
| Shared React components, layout, accessibility, dialogs or previews | [astra-ui](https://github.com/LightconeResearch/astra-ui) | Rendering supplied data; the host owns loading, networking and refresh. |
| MySTRA roles/directives, references, live values or ASTRA-to-MyST conversion | [MySTRA](https://github.com/LightconeResearch/MySTRA) | Report content/build conversion. |
| Book/article publication layout, navigation or theme overlay | [astra-theme](https://github.com/LightconeResearch/astra-theme) | Source for the generated astra-book-theme and astra-article-theme repos. |
| Instructions, navigation or broken links on docs.lightconeresearch.org | [docs](https://github.com/LightconeResearch/docs) | Include the exact page; correct instructions exposing a tool bug belong to that tool. |
| This reporting skill, genuinely unclear ownership, or feedback spanning the stack | [feedback](https://github.com/LightconeResearch/feedback) | Fallback when no single product owner is supported by the evidence. |

A failure inside a researcher's own script is not by itself a Lightcone defect.
Describe the observed boundary without inventing a diagnosis. If context is too
vague even to describe a symptom, ask about the action and result before filing.
For an unlisted product, consult its official docs or source README; don't guess
from an old name. Do not move an inaccessible/private report to a public fallback
without the user's approval and a safe draft.

The [stack overview](https://docs.lightconeresearch.org/) explains the products;
the linked source READMEs explain ownership. Recheck them if evidence conflicts
with this map. Repo labels are independent: use `feedback` where permitted and
verify it was applied. Missing label permissions must not prevent a useful report.
