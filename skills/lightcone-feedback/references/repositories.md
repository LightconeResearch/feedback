# Where to file Lightcone feedback

Repository names and public visibility checked on 2026-10-15. Verify the selected
destination before posting; package names and repository names are not interchangeable.
The links in this table lead to each source repository and its current README.

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

## Choosing at the seams

- **Schema versus implementation:** a rule or field defined incorrectly belongs
  in astra-spec. A Python implementation mishandling a valid spec belongs in
  astra-tools; its TypeScript counterpart belongs in astra-typescript. Capture
  the installed schema/tool versions when available. A shared `astra.*` Python
  namespace alone does not distinguish the two Python distributions.
- **Lab versus CLI:** if materialization fails directly in `lc`, use lightcone-cli.
  If Lab cannot invoke a working command or display its output, start with Lab.
  A traceback identifying a dependency can justify another route without rerunning.
- **UI versus SDK:** incorrect resolved data/bindings points to the SDK; correctly
  supplied data displayed incorrectly points to the UI. A file/network loading
  problem points to the host. Without that evidence, report the visible host symptom.
- **Report versus theme:** wrong content produced from an ASTRA role/directive
  points to MySTRA. Correct content styled or navigated incorrectly points to
  astra-theme. Isolated shared React component defects can go to astra-ui.
- **Agent versus tool:** a skill generating an obsolete command points to
  agent-skills; a valid command crashing points to the command's repository.
- **Research code:** a traceback in the user's recipe alone is not proof of a
  Lightcone defect. Describe the boundary and uncertainty; do not invent one.

Choose one primary issue and mention relevant related components. Do not file
duplicates across repos. For an unresolved cross-stack report, propose the repo
owning the entry point the tester used, state the uncertainty, and show the choice
with the draft. If even the entry point is unknown, ask one short question about
what they were using instead of silently defaulting everything to lightcone-cli.

## Other products and inaccessible repositories

For a product not listed here (such as a hosted deployment or editor extension),
inspect its current official docs, package repository metadata or source README
for an issue destination. Old product names are not enough to identify a repo.
Do not guess a public fallback for an inaccessible repository. Finish a redacted
draft and let the tester use their existing beta support channel if access is absent.

For a bug in this standalone feedback skill, use its distribution repository if
known from installation metadata or the user. Do not assume it is maintained in
agent-skills while it is distributed separately.

## Sources and maintenance

Use the [stack overview](https://docs.lightconeresearch.org/), its
[ASTRA](https://docs.lightconeresearch.org/astra),
[CLI](https://docs.lightconeresearch.org/lightcone-cli),
[Lab](https://docs.lightconeresearch.org/lightcone-lab),
[MySTRA](https://docs.lightconeresearch.org/mystra), and
[agent skills](https://docs.lightconeresearch.org/agent-skills) pages for product
context. The source READMEs linked above establish the implementation boundaries.
Recheck them when evidence conflicts with this map. Avoid fixed release-version
claims: the tester's installed version is what matters for the report.
