# Decision Log

This file records the decision process rather than only the final model. A rerunnable model is not the same as a reproducible decision.

## Evidence classes

1. **Observed** — portal inputs and returned outputs.
2. **Prospective** — forecasts or rationale written before the portal result.
3. **Retrospective** — later challenger analyses using historical data.
4. **Interpretive** — conclusions drawn after comparing prediction with observation.

Retrospective analysis never overwrites the historical record, and unsubmitted counterfactual candidates never receive invented portal outcomes.

## Methodological evolution

| Stage | Decision rule | What changed |
|---|---|---|
| Early | GP / acquisition-led | Built the sequential BO baseline and exploration/exploitation discipline |
| Middle | Function-specific diagnostics | Added alternative kernels/models, local search and controlled probes |
| Validation | Forecast-led authority | Used rolling/prospective performance to decide when the surrogate deserved influence |
| Current | Evidence-gated committee | GP/local/structural/HEBO/TuRBO challengers compete; the final query is chosen by evidence, not algorithm prestige |

## Current best through Week 9

- F1: 1.92128078806402e-15 at `0.729874-0.731800` (Week 9).
- F2: 0.691314866323759 at `0.701500-0.959816` (Week 6).
- F3: -0.0208561545295093 at `0.487816-0.639038-0.365586` (Week 6).
- F4: 0.658932867221058 at `0.420380-0.427768-0.368794-0.412497` (Week 9).
- F5: 6583.56144525802 at `0.858373-0.999999-0.999999-0.999999` (Week 9).
- F6: -0.541447831970796 at `0.481359-0.256800-0.814241-0.999999-0.057285` (Week 4).
- F7: 1.78633819779689 at `0.228702-0.369270-0.256273-0.262985-0.391467-0.834089` (Week 9).
- F8: 9.9324430095864 at `0.128076-0.104109-0.074587-0.102502-0.970754-0.314560-0.238989-0.536764` (Week 9).

## Round 10 governance and final submission

Each proposed query must have a credible prospect of improvement **or** produce information that changes a later decision. Historical forecast accuracy and direct observations take precedence over algorithm prestige. This is a documented human review policy rather than a calibrated automatic acceptance rule.

**The Round 10 vectors are now confirmed as submitted**, but none has an observed score in the dataset. Four earlier provisional ideas (F1, F3, F6 and F7) were replaced. The old points are preserved alongside final choices and their evidential rationale in [the revision audit](../reports/round10_revision_audit.md). F2, F4, F5 and F8 were unchanged.

**F8's predicted output of 10 remains a structural model result until the portal returns its score.** F6 and F7's higher model-predicted means are not measured improvements. Some exploratory candidate selection was informed by public classmates' evaluated data; these are external benchmarks, not observations collected by this participant, and their assessed use is subject to the course collaboration rules.

[The exact submitted vectors](../experiments/round_10/queries.txt) are recorded separately from observed results. The archive of Weeks 1–9 has not been rewritten.

Transparency is the ability to tell what was known, what was assumed, what was decided and what happened next, rather than the volume of generated documentation.
