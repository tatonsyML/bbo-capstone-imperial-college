# Round 12 | Model comparisons, F6 and F7 improvements

**Status:** The eight returned portal scores were confirmed. R12 improved F6 and F7, while several functions repeated earlier inputs.

## My reasoning at the time

I began the challenge with broad Gaussian-process searches and substantial kernel tuning. By this week I separated data preparation, prospective validation and candidate selection. F2's Week 9 forecast of about 0.731 and return near 0.506 had made me much less willing to trust an attractive predicted improvement without chronological testing and sensitivity checks.

Principal Component Analysis was useful precisely because it challenged a tempting simplification. For F8 I analysed 52 input vectors: 40 starting observations and 12 submitted queries. Two principal components retained 48.8% of sampled input variance, while seven retained 95.3%. PC1 gave substantial weights to inputs 1 and 3, approximately 0.493 and 0.430; PC2 weighted input 8 strongly, approximately 0.630. Yet input variance is not the same as objective sensitivity. My fitted quadratic suggested a direction could matter greatly to the score even when it accounted for little variation in the sampled inputs.

I tested compression within the fitted quadratic. Restricting the modelled search to the first two PCs limited the maximum to 9.955973. Seven components allowed 9.999974, still below the unconstrained value of 10. A separate retrospective fit based on the original forty F8 observations accurately reproduced later returns. That supported the structural explanation but had to remain labelled retrospective: it was a different evidential claim from a forecast recorded before submission.

Other functions supplied complementary lessons. F4 had stalled near 0.659 during microscopic steps, while a wider local movement eventually reached 0.730459. F6 improved from about −0.123761 to −0.037519 through a coordinated change, but because several inputs moved together I did not attribute the gain to a single coordinate. F7 reached another measured best. Four repeated queries confirmed their previous values but added no new locations to the input history.

For the final round I wanted to compare predicted improvement with known forecast error and use remaining queries to test the highest-value unresolved questions. Simplification was worthwhile only when it preserved decisions. In a practical analogy from payroll-risk analytics, a low-variance input may represent a rare and costly signal, and discarding it because PCA gives it little weight would be a mistake. I had learnt to simplify the representation only after checking what the simplification lost.

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

## How I approached this round

I tested whether PCA retained useful search information. For F8, two PCs captured **48.8%** of the input variance and seven captured **95.3%**, but constraining the quadratic reduced the modelled maximum to **9.955973** (two PCs) or **9.999974** (seven) rather than **10**. The portal recorded **F6/F7 improvements**, repeated inputs and underperforming F2/F3 queries. The [Week 12 modelling scripts](original/review_round12.py) show how I compared methods and selected candidate inputs.


## Original evidence

[Returned values](outputs.txt) · [R11–12 portal CSV](../../data/portal_rounds_11_12.csv) · [observed history](../../data/all_observations.csv). The full Round 12 input list is captured in the combined portal file.

## Week 12 modelling and optimisation code

I ran a model-comparison and candidate-selection study for **F2, F3, F4 and F6**. I tested alternative surrogate models, data transformations, model robustness and local search, using earlier portal results and separately identified participant observations. The analysis produced the candidate shortlist used for the Round 12 submissions.

| Python implementation | Methods and questions investigated | Results |
|---|---|---|
| [review_round12.py](original/review_round12.py) | Matérn/RBF/ARD GP, output warping, Extra Trees, PCA/kernel PCA, PLS, Bayesian Ridge, MLP; source-held-out checks; robust committee, EI/UCB, candidate-pool selection and input-space diagnostics | [Model results](original/week12_original_assets.zip) |
| [robust_and_warp.py](original/robust_and_warp.py) | Source-exclusion comparisons and experimental input/output warping to test stability of predictions | [Robustness results](original/week12_original_assets.zip) |
| [tpe_local.py](original/tpe_local.py) | Real Optuna TPE suggestions (independent and multivariate), plus local regularised quadratic analysis for F4 | [TPE/local results](original/week12_original_assets.zip) |
| [trust_region_ts.py](original/trust_region_ts.py) | Success/failure trust-region updates, local Matérn GP and posterior Thompson-sampling proposals | [Trust-region results](original/week12_original_assets.zip) |

The first and third rows are not interchangeable: **Optuna TPE was used**, whereas the HEBO-style warping/committee and TuRBO-style trust-region components are **inspired by those algorithms, not complete official HEBO or TuRBO implementations**.

### Candidate selection and measured outcomes

The [candidate comparison](original/week12_candidate_comparison_2026-11-02.csv) and [selected input vectors](original/week12_final_points_2026-11-02.txt) record the recommendations from the modelling analysis. **All eight match the actual Round 12 submissions** in the [portal results](../../data/portal_rounds_11_12.csv). Predicted and measured scores are kept separate.

- **F2:** robust committee favoured `0.684399-0.368552`. The forecast edge was small and the portal later returned **0.660671151390024**, below the Round 11 best.
- **F3:** validation included independent participant data and model disagreement. The submitted `0.313581-0.474345-0.485191` returned **−0.0226526646178297**. Its peer-reported score was not a guaranteed portal result.
- **F4:** cross-model extrapolation was unreliable; the decision was to **repeat** the confirmed Round 11 point at **0.7304594213260924**.
- **F6:** a robust committee candidate `0.415080-0.344119-0.644062-0.776818-0.076258` produced a **new personal best −0.03751864724436928**, improving the prior Round 11 score **−0.12376148016289273**.
- **F1, F5, F7, F8:** this four-script review did **not** retrain their candidate generators. Those selections used previously established analytical/structural evidence; the confirmed **F7 Round 12** input and score are in the table above.

This is a *selection-evidence connection*, not proof that all reported numerical model forecasts were calibrated. The model comparisons include **peer-published observations**, separately identified from my own portal evaluations; the [research notes](original/week12_full_review_2026-11-02.md) explain their role and limitations. The included cross-cohort checks are retrospective diagnostics and not new black-box evaluations. The peer-data redistribution and programme requirements should be checked before reusing this material for formal assessment.

### Run the analysis

The [`original/`](original/review_round12.py) scripts preserve the modelling implementation and settings. The [`portable/`](portable/review_round12.py) versions change **only** the working-directory path so the same experiments run from a cloned repository. The algorithms and hyperparameters are unchanged.

The [data and results archive](original/week12_original_assets.zip) contains the numerical observations, four JSON reports, candidate comparison and selected inputs. Integrity tests check the files against their expected hashes: [test_round12_historical_archive.py](../../tests/test_round12_historical_archive.py).

To prepare portable execution from a cloned repository:

```bash
python -m pip install -r journey/round_12/requirements.txt
python journey/round_12/portable/bootstrap_assets.py
cd journey/round_12/portable
python review_round12.py
python robust_and_warp.py
python tpe_local.py
python trust_region_ts.py
```

The bootstrap extracts only three archived `bbo_verified_F{2,3,6}.txt` transcripts into the portable working folder, with checksums and no overwrite of modified files. F4 source rows remain embedded in the original script. Full reruns are **computationally intensive**; the archive's historical JSON files are preserved as *saved results*, not claimed as fully independently reproduced here.

**Validation:** All four scripts and their portable counterparts passed syntax checks. GP data-loading and selected fitting routines ran successfully, and the proposed inputs match the recorded submissions. The full computationally intensive modelling sweeps have **not** been independently rerun.

## What the experiments taught me

By the end of Round 12, I had **271 observed scores**. The findings below informed my final-round strategy.

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

## Evidence categories

**Portal:** personally selected, returned result. **Prospective:** forecast recorded before result. **Retrospective:** equation fit or analysis performed afterwards. **External:** publicly shared results used for model comparisons or checking, not counted as personal queries. **Hypothesis:** unconfirmed conjecture or Round 13 candidate.

[Provenance](../../DATASHEET.md) · [Structural reconstruction](../../docs/functions.md) · [Portal log](../../data/portal_rounds_11_12.csv).
