# Maintainer component map

All beta reports stay in the shared feedback inbox. This map helps maintainers
identify likely implementation owners; testers and the reporting skill do not
need to select a repository. Link any implementation issue or pull request back
to the original beta report so the reporter has one place to follow progress.

These public source repositories and their issue availability were checked on
2026-10-15. Recheck ownership before assigning implementation work. Identify the
product from the report; treat a dependency as the cause only when evidence
supports it. A missing environment detail is not a reason to invent a diagnosis.

## Ownership map

| Evidence points to… | Repository | Boundary |
| --- | --- | --- |
| ASTRA format, field definitions, schema/generated model constraints, specification ambiguity or proposed format changes | [astra-spec](https://github.com/LightconeResearch/astra-spec) | Owns the format, not recipe execution. Schema/format docs belong here. |
| `astra` CLI, Python validation or resolution, scaffolding, paper cache, evidence/quote checks | [astra-tools](https://github.com/LightconeResearch/astra-tools) | Python tooling; never executes analysis recipes. The historical `ASTRA` repo URL redirects here. |
| `lc` initialization, execution, environments, sandbox/container failures, materialization, freshness, provenance, git-annex/DataLad integration, cluster jobs | [lightcone-cli](https://github.com/LightconeResearch/lightcone-cli) | Owns execution and its records. A known Python semantic-validation failure belongs in astra-tools. |
| Skill instructions, plugin packaging/installation, command guidance, validation-hook dispatch | [agent-skills](https://github.com/LightconeResearch/agent-skills) | Report faulty instructions/hooks here; report correctly invoked tools failing to their owners. |
| Lightcone Lab project Home, Jupyter integration, agent launch/chat, refresh, loading files/artifacts/papers, host routing | [jupyterlab-lightcone](https://github.com/LightconeResearch/jupyterlab-lightcone) | Default for a Lab symptom when no dependency has been isolated. |
| `@astra-spec/sdk`, JavaScript/TypeScript validation/resolution, resolved document contract, artifact bindings or canonical paths | [astra-typescript](https://github.com/LightconeResearch/astra-typescript) | Independent of the Python validator. Prefer direct SDK evidence over guessing from a UI symptom. |
| Shared React components: layout, accessibility, record dialogs, hover previews, rendering supplied data | [astra-ui](https://github.com/LightconeResearch/astra-ui) | Presentation only. Hosts own I/O, network requests, refresh and application state. |
| MySTRA roles/directives, ASTRA references in MyST, live values, ASTRA-to-MyST build output | [MySTRA](https://github.com/LightconeResearch/MySTRA) | Publication adapter, not the whole interactive workbench. Preserve the repository's casing. |
| ASTRA book/article theme layout, navigation, theme integration or publication overlay | [astra-theme](https://github.com/LightconeResearch/astra-theme) | Source for astra-book-theme and astra-article-theme; those two repos contain generated builds and direct issues to the source. |
| Broken links, misleading walkthroughs, navigation or content on docs.lightconeresearch.org | [docs](https://github.com/LightconeResearch/docs) | Include the exact page URL. A correct instruction exposing a tool bug belongs to that tool. |

All destinations above were public with issues enabled when checked. This is not
a guarantee about future visibility or a tester's permission to post.

## Boundaries that matter

- The format is astra-spec; Python behavior is astra-tools; JavaScript behavior
  is astra-typescript. The historical ASTRA repository redirects to astra-tools.
- Lab owns host integration and loading. The CLI owns execution. Shared React
  rendering is astra-ui; incorrectly resolved data may belong to the SDK.
- MySTRA owns publication content conversion. astra-theme owns the book/article
  presentation and publishes the generated theme repositories.
- Faulty instructions or hook dispatch belong to agent-skills; a correctly
  invoked command failing belongs to that tool.

See the [stack overview](https://docs.lightconeresearch.org/) and each source
README above for current architecture. Versions in a beta report should describe
the failing installation, not the latest release.
