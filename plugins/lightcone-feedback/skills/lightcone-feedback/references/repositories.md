# Lightcone repository map

Choose one of these seven reporting destinations based on the product the tester
used. Testers do not need to diagnose ownership. Explain the choice briefly in the
report preview; verify visibility and issue availability before submission.

| Feedback about | Repository |
| --- | --- |
| `lc` setup, execution, environments, containers, provenance or cluster jobs | [lightcone-cli](https://github.com/LightconeResearch/lightcone-cli) |
| Skills, plugins, hooks or agent guidance, including this feedback skill | [agent-skills](https://github.com/LightconeResearch/agent-skills) |
| ASTRA fields, schema constraints, specification ambiguity or format changes | [astra-spec](https://github.com/LightconeResearch/astra-spec) |
| `astra` CLI, Python validation/resolution, scaffolding or paper/evidence tools | [astra-tools](https://github.com/LightconeResearch/astra-tools) |
| Shared UI rendering, layout, accessibility, dialogs or previews | [astra-ui](https://github.com/LightconeResearch/astra-ui) |
| Lab Home, Jupyter integration, agent launch/chat or loading/refreshing files | [jupyterlab-lightcone](https://github.com/LightconeResearch/jupyterlab-lightcone) |
| Report content, roles/directives, live values, MyST builds or publication styling | [MySTRA](https://github.com/LightconeResearch/MySTRA) |

Keep documentation feedback with the product it describes and include the page URL;
use agent-skills for general onboarding or agent guidance. Publication/theme issues
go to MySTRA. TypeScript internals stay with the affected product; include evidence
of a suspected dependency defect without rerouting to astra-typescript. The docs,
astra-theme and feedback repos are not reporting destinations in this map.

For Lab symptoms, default to jupyterlab-lightcone; choose astra-ui only when the
problem is clearly in shared rendering rather than loading or refresh. For feedback
spanning products, use the main affected product and name the others in the body.
If the affected product is unknown, ask what the tester was using rather than
choosing a generic inbox. Respect an explicitly requested destination.

A failure in a researcher's own script is not by itself a Lightcone defect.
Describe observations without inventing a diagnosis. Do not move an inaccessible
or private report to a public repository without approval and a safe draft.
