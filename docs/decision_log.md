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

## Round 10 governance

Each candidate must satisfy at least one of two tests: it should have credible upside, or it should resolve an uncertainty that changes the next decision. Strong local validation outranks a more sophisticated model that has recently failed.

The exact F1, F3 and F6 restart coordinates in the working configuration are provisional and must be rerun before portal submission. F8's predicted value of 10 is a structural hypothesis until the portal tests it.

Transparency is not the volume of documentation. It is the ability to tell what was known, what was assumed, what was decided and what happened next.
