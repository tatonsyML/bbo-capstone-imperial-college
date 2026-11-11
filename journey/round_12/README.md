# Round 12 | Structural forecast verification and F6 recovery

**Status:** The eight returned portal scores were confirmed. R12 improved F6 and F7, while several functions repeated earlier inputs.

## What I did and what happened

| Function | Actual input | Returned score |
|---|---|---:|
| F1 | 0.628540-0.628540 | 1.9999999996761817 |
| F2 | 0.684399-0.368552 | 0.660671151390024 |
| F3 | 0.313581-0.474345-0.485191 | -0.0226526646178297 |
| F4 | 0.415000-0.417000-0.366500-0.413000 | 0.7304594213260924 |
| F5 | 0.999999-0.999999-0.999999-0.999999 | 8662.405001248297 |
| F6 | 0.415080-0.344119-0.644062-0.776818-0.076258 | -0.03751864724436928 |
| F7 | 0.201689-0.150011-0.476874-0.275332-0.311652-0.657301 | 3.3223680113931557 |
| F8 | 0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000 | 10 |

F7's positive Hartmann-6 forecast of about **3.32236801** was recorded before receiving the Round 12 score of **3.3223680113931557**.

## What I learnt

Repeats confirmed the same values without exploring new input regions. A pre-result structural forecast is more informative than matching a function only after seeing its score.

## Original evidence

[Returned values](outputs.txt) · [R11–12 portal CSV](../../data/portal_rounds_11_12.csv) · [observed history](../../data/all_observations.csv). The full Round 12 input list is captured in the combined portal file.

## Detailed Round 12 analysis (dated snapshot)

The following evidence was recorded with **271 known scores** before the Round 13 returns arrived. It is retained as the analysis available at that stage, not the current final-best table.

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
- **Evidence correction (verified from the original results email):** the Round 11 F7 input was subsequently recovered as `0.233000-0.128000-0.522000-0.276000-0.310000-0.667000` and its result was `3.278967926227992`. The dated snapshot originally lacked the input. It is now confirmed in the [Round 11 evidence](../round_11/README.md) and [canonical CSV](../../data/all_observations.csv). The *original candidate-selection script* is still not retained.

## Evidence categories

**Portal:** personally selected, returned result. **Prospective:** forecast recorded before result. **Retrospective:** equation fit or analysis performed afterwards. **External:** publicly shared results used for model comparisons or checking, not counted as personal queries. **Hypothesis:** unconfirmed conjecture or Round 13 candidate.

[Provenance](../../DATASHEET.md) · [Structural reconstruction](../../docs/functions.md) · [Portal log](../../data/portal_rounds_11_12.csv).

