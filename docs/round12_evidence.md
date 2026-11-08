# Verified evidence through Round 12

The latest verified evidence includes 175 initial course observations plus 12 returned rounds × eight functions = **271 evaluations**, including repeated coordinates. Round 13 outputs are not verified.

## Best-so-far outcomes

| Function | Final verified best | First attained |
|---|---:|---|
| F1 | 1.9999999996761817 | R11 |
| F2 | 0.6953368270741286 | R11 |
| F3 | -0.005709220275560069 | R11 |
| F4 | 0.7304594213260924 | R11 |
| F5 | 8662.405001248297 | R10 |
| F6 | -0.03751864724436928 | R12 |
| F7 | 3.3223680113931557 | R12 |
| F8 | 10 | R10 |

All eight final bests were established during Rounds 10–12. [Full result CSV](../reports/current_best_after_week12.csv) includes inputs and Round 9 comparisons. Scores use different scales and should not be aggregated.

## Three different problems, three evidence-based changes

**F2 — predictive failure:** a recorded prospective forecast of 0.730502 returned **0.505526** (error ≈0.224976). The observed miss motivates model comparison; one error does not prove universal GP miscalibration.

**F4 — inaccurate search strategy despite an accurate local prediction:** one model forecast agreed with the next return to about **1.56 × 10^-9**. A change of 0.000001 in one coordinate raised the output only from 0.658930 to 0.658962. A broader Round 11 local step reached **0.7304594213260924**. Accurate interpolation near a chosen point did not mean the search was wide enough.

**F8 — unnecessary model complexity:** a GP forecast was already accurate to around 0.000025, yet a 17-coefficient additive quadratic explained F8, exposing an analytic optimum at 10. Its vertex was portal-confirmed. The model was fitted from accumulated personal observations, then supported by five public external input-output checks before the Round 10 portal submission. A *separate retrospective experiment* fitted only the 40 original course observations and predicted all 12 later personal returns to numerical precision.

The diagnostic rule is to ask separately: (1) has the model predicted unseen results reliably, (2) is the search region adequate, and (3) is the mathematical representation suitable?

## F7 and PCA

Round 12 F7's positive Hartmann-6 structural recommendation was recorded *before* the return, with predicted 3.32236801. The portal returned **3.3223680113931557** at the actual submitted coordinate. This is a successful specific prediction, not authentication of the unknown source code.

The first two principal components of sampled F8 coordinates explained **48.8% of input variance**. Restricting the fitted quadratic to them reduced its model-predicted optimum to approximately **9.955973**, compared with 10 in the full eight-dimensional space. PCA does not directly optimise the objective.

## Round 12 controls

- Four input repeats (F1, F4, F5 and F8) returned identical scores, confirming repeatability at those settings without exploring nearby inputs.
- Four new points returned two gains (F6, F7) and two worse scores (F2, F3).
- The actual submitted F2/F3/F6 inputs differ from an older R12 modelled shortlist; do not attach those older means to the actual portal returns.
- Round 11 F7's return was 3.27896792623, but its exact coordinate is missing from the source snapshot. This gap is flagged, not filled with a guessed point.

## Evidence categories

**Portal:** personally selected, returned result. **Prospective:** forecast recorded before result. **Retrospective:** equation fit or analysis performed afterwards. **External:** publicly shared results used for model comparisons or checking, not counted as personal queries. **Hypothesis:** unconfirmed conjecture or Round 13 candidate.

[Provenance](evidence_provenance.md) · [Structural reconstruction](structural_reconstruction.md) · [Portal log](../data/portal_rounds_11_12.csv).
