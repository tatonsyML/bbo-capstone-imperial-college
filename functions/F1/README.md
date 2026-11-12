# Function 1 · Finding a signal in apparent numerical silence

[← All functions](../README.md) · [Project home](../../README.md) · [Observed inputs and outputs](observations.csv) · [Complete decision ledger](selection_history.csv)

**2 inputs · 10 starting observations · 13 rounds**

| Initial best | Final best | First achieved | Best input |
|---:|---:|:---:|---|
| `7.710875114502849e-16` | **`1.9999999996761817`** | **Round 11** | `0.628540-0.628540` |

## Understanding this function

Almost every early response was extremely close to zero. The first GP and UCB proposals could not locate a useful region, and local improvements around a weak incumbent were misleading. Contemporary notes describe a Gaussian-modulated structural hypothesis and some external exploration around Round 10–11; those historical records are preserved below. **A separate retrospective reconstruction is now fully reproducible using only my own recorded F1 observations.** Its mathematical form was supplied separately; this numerical fit does not reproduce the original Round 11 candidate-selection process.

### Score progression from real evaluations

![Function 1 measured best-so-far history](progress.svg)

The chart tracks measured best-so-far results. A flat interval means no improvement to the incumbent, not that a model predicted a constant function.

## Weekly development · expand a round

Each round shows **what was known or being tested, what was submitted, what returned, and what was learnt**. The original 52-page weekly reflection is the narrative foundation; the decision ledger, surviving code and official portal records establish what was actually submitted. An exact historic kernel/seed/forecast appears only if retained. Where early rationale was reconstructed later, it is explicitly labelled in the ledger.

**How to read the evidence:** Each round links to its saved inputs, portal returns and the actual code or analysis available for that period. An original script, a notebook with recorded selections, and a later reconstruction are different kinds of evidence. The [round-by-round source audit](../../docs/WEEKLY_SUBMISSION_EVIDENCE.md#original-code-and-decision-evidence) explains those distinctions.

<details>
<summary><strong>Round 1 · Opening hypothesis</strong> — 0.00000000</summary>

**Original learning context:** The first reflection described F1 as nearly all zero and chose an under-sampled area because no useful local peak had been established.

**Strategy / candidate-selection evidence:** GP and acquisition baseline (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.02-0.98`  
**Actual portal result:** `0.0`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Second round: GP/UCB with per-function exploration weights; deterministic candidate grids or pools.

**Code and evidence:** [Round 1 reflection and portal evidence](../../journey/round_01/README.md) · [Submitted inputs](../../journey/round_01/queries.txt) · [Returned scores](../../journey/round_01/outputs.txt) · [Original coursework notebook](../../journey/round_01/supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb) (coursework, not a verified portal generator) · No separate candidate-generator source authenticated · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 2 · GP and UCB working package</strong> — -1.96324543e-233</summary>

**Original learning context:** After the first query returned zero, the original Week 2 reflection gave F1 the largest UCB exploration weight, κ=3.0, and considered a future signal/no-signal classifier without claiming it was already implemented.

**Strategy / candidate-selection evidence:** GP and UCB working package *(early-round attribution partly retrospective)*.

**Submitted input:** `0.052001-0.865999`  
**Actual portal result:** `-1.9632454298284602e-233`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Third round: function-specific EI/UCB policy; 1%-of-output-SD EI margin and GP fitting restarts documented at pipeline level.

**Code and evidence:** [Round 2 reflection and portal evidence](../../journey/round_02/README.md) · [Submitted inputs](../../journey/round_02/queries.txt) · [Returned scores](../../journey/round_02/outputs.txt) · [Original GP/UCB selection script](../../journey/round_02/week2_ucb_course_aligned.py) · [Eight saved selections](../../journey/round_02/week2_ucb_results.csv) (all eight saved portal values match the submitted record) · [Notebook](../../journey/round_02/Capstone_BBO_Week2_UCB_only.ipynb) · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 3 · Function-specific EI or wider search (retrospective)</strong> — 2.69213109e-65</summary>

**Original learning context:** Third round: function-specific EI/UCB policy; 1%-of-output-SD EI margin and GP fitting restarts documented at pipeline level.

**Strategy / candidate-selection evidence:** Function-specific EI or wider search (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.636406-0.206433`  
**Actual portal result:** `2.69213108614911e-65`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Fourth round: GP paired with SVM good/bad checks and small neural-network gradient challengers, not hard classifier exclusion.

**Code and evidence:** [Round 3 reflection and portal evidence](../../journey/round_03/README.md) · [Submitted inputs](../../journey/round_03/queries.txt) · [Returned scores](../../journey/round_03/outputs.txt) · The original reflection records function-specific acquisition choices; no standalone original query generator is preserved for this round · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 4 · GP, SVM and neural-network diagnostics</strong> — 1.51764873e-192</summary>

**Original learning context:** Fourth round: GP paired with SVM good/bad checks and small neural-network gradient challengers, not hard classifier exclusion.

**Strategy / candidate-selection evidence:** GP, SVM and neural-network diagnostics *(early-round attribution partly retrospective)*.

**Submitted input:** `0.999999-0.999999`  
**Actual portal result:** `1.517648729565899e-192`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Fifth round: use controlled coordinate differences to avoid confusing a multi-variable shift with a causal single-input effect.

**Code and evidence:** [Round 4 reflection and portal evidence](../../journey/round_04/README.md) · [Submitted inputs](../../journey/round_04/queries.txt) · [Returned scores](../../journey/round_04/outputs.txt) · [Original analysis code](../../journey/round_04/capstone_bbo_week4_module15.py) · [Executed notebook](../../journey/round_04/Capstone_BBO_Week4_Module15.ipynb) (final eight inputs stored explicitly; hybrid selection, not an autonomous selector) · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 5 · Controlled coordinate probes (retrospective)</strong> — 1.33191455e-22</summary>

**Original learning context:** Fifth round: use controlled coordinate differences to avoid confusing a multi-variable shift with a causal single-input effect.

**Strategy / candidate-selection evidence:** Controlled coordinate probes (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.75-0.75`  
**Actual portal result:** `1.3319145509281447e-22`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Sixth round: compare GP and MLP using five-fold cross-validated error; treat extra model flexibility as something to justify.

**Code and evidence:** [Round 5 reflection and portal evidence](../../journey/round_05/README.md) · [Submitted inputs](../../journey/round_05/queries.txt) · [Returned scores](../../journey/round_05/outputs.txt) · Contemporary reflection and submitted measurements preserved; no standalone selection code authenticated · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 6 · GP, ridge and MLP comparison; controlled local fit</strong> — 3.25547512e-17</summary>

**Original learning context:** Sixth round: compare GP and MLP using five-fold cross-validated error; treat extra model flexibility as something to justify.

**Strategy / candidate-selection evidence:** GP, ridge and MLP comparison; controlled local fit *(early-round attribution partly retrospective)*.

**Submitted input:** `0.732524-0.7389`  
**Actual portal result:** `3.2554751168755075e-17`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Near-zero results still held almost no meaningful signal; the Week 7 paper prioritised ARD kernels and checking how well forecasts survived the next portal return.

**Code and evidence:** [Round 6 reflection and portal evidence](../../journey/round_06/README.md) · [Submitted inputs](../../journey/round_06/queries.txt) · [Returned scores](../../journey/round_06/outputs.txt) · [Original Module 17 notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) · [Eight selected inputs](../../journey/round_06/results/round6_queries.csv) · [Decision rationale](../../journey/round_06/results/round6_query_rationale.csv) (standalone fitter source not retained) · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 7 · ARD and local forecast investigations (retrospective)</strong> — 1.31425296e-15 ★ new best</summary>

**Original learning context:** Near-zero results still held almost no meaningful signal; the Week 7 paper prioritised ARD kernels and checking how well forecasts survived the next portal return.

**Strategy / candidate-selection evidence:** ARD and local forecast investigations (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.730874-0.7318`  
**Actual portal result:** `1.3142529628112004e-15`  
**Best observed before → after:** `7.710875114502849e-16` → `1.3142529628112004e-15`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. Eighth round: separate LLM hypothesis generation from deterministic numerical validation and check candidate precision.

**Code and evidence:** [Round 7 reflection and portal evidence](../../journey/round_07/README.md) · [Submitted inputs](../../journey/round_07/queries.txt) · [Returned scores](../../journey/round_07/outputs.txt) · [Next-round audit of Week 7 forecasts](../../journey/round_08/results/week7_audit.csv) (subsequent analysis, not the original Round 7 generator) · No authenticated standalone Round 7 selector · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 8 · Rank-GP local consensus around the new Week 7 best; stay inside the near-zer…</strong> — 4.19700395e-16</summary>

**Original learning context:** Eighth round: separate LLM hypothesis generation from deterministic numerical validation and check candidate precision.

**Strategy / candidate-selection evidence:** Rank-GP local consensus around the new Week 7 best; stay inside the near-zero basin while testing a small x1-up/x2-down move..

**Submitted input:** `0.735874-0.729467`  
**Actual portal result:** `4.1970039548686525e-16`  
**Best observed before → after:** `1.3142529628112004e-15` → `1.3142529628112004e-15`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. A cautious one-coordinate change was chosen while the output scale remained pathological; I had not yet located the main positive-response region.

**Code and evidence:** [Round 8 reflection and portal evidence](../../journey/round_08/README.md) · [Submitted inputs](../../journey/round_08/queries.txt) · [Returned scores](../../journey/round_08/outputs.txt) · [Original Module 19 Python analysis](../../journey/round_08/capstone_bbo_module19_round8.py) · [Original eight-input decision record](../../journey/round_08/results/round8_queries.csv) (all eight match portal inputs) · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 9 · One-coordinate probe: move x1 down by 0.001 from the Week 7 incumbent while…</strong> — 1.92128079e-15 ★ new best</summary>

**Original learning context:** A cautious one-coordinate change was chosen while the output scale remained pathological; I had not yet located the main positive-response region.

**Strategy / candidate-selection evidence:** One-coordinate probe: move x1 down by 0.001 from the Week 7 incumbent while holding x2 fixed. The updated rank-GP committee favours lower x1, but the output scale is too pathological for a trustworthy numeric forecast..

**Submitted input:** `0.729874-0.7318`  
**Actual portal result:** `1.921280788064022e-15`  
**Best observed before → after:** `1.3142529628112004e-15` → `1.921280788064022e-15`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The original Round 10 plan explicitly left the repeated (0.73,0.73) neighbourhood, using external evidence to challenge the stale local hypothesis.

**Code and evidence:** [Round 9 reflection and portal evidence](../../journey/round_09/README.md) · [Submitted inputs](../../journey/round_09/queries.txt) · [Returned scores](../../journey/round_09/outputs.txt) · [Dated eight-input decision and forecast ledger](../../journey/round_09/results/round9_queries.csv) (all eight match portal inputs) · The preserved local-fitting script does not generate F1's recorded query · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 10 · Targeted positive-response region; exploratory near-peer evidence; unobserved</strong> — 0.00000726400118 ★ new best</summary>

**Original learning context:** The original Round 10 plan explicitly left the repeated (0.73,0.73) neighbourhood, using external evidence to challenge the stale local hypothesis.

**Strategy / candidate-selection evidence:** Targeted positive-response region; exploratory near-peer evidence; unobserved.

**Submitted input:** `0.582552-0.558941`  
**Actual portal result:** `0.000007264001184177771`  
**Best observed before → after:** `1.921280788064022e-15` → `0.000007264001184177771`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. A two-component Gaussian-modulated oscillatory explanation was checked against prior recorded observations before selecting the new point.

**Code and evidence:** [Round 10 reflection and portal evidence](../../journey/round_10/README.md) · [Submitted inputs](../../journey/round_10/queries.txt) · [Returned scores](../../journey/round_10/outputs.txt) · [Dated final candidate list](../../journey/round_10/round10_candidates.csv) · [Pre-result planning snapshot](../../journey/round_10/optimisation.yaml) · [GP/HEBO-inspired/TuRBO-style challenger code](../../src/bbo/optimizer.py) (not proof of the exact final per-function generator) · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 11 · Alternative-region exploration and structural investigations</strong> — 2.00000000 ★ new best</summary>

**Original learning context:** A two-component Gaussian-modulated oscillatory explanation was checked against prior recorded observations before selecting the new point.

**Strategy / candidate-selection evidence:** Alternative-region exploration and structural investigations.

**Submitted input:** `0.628540-0.628540`  
**Actual portal result:** `1.9999999996761817`  
**Best observed before → after:** `0.000007264001184177771` → `1.9999999996761817`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The same high-scoring coordinates were deliberately repeated, providing little new coverage.

**Code and evidence:** [Round 11 reflection and portal evidence](../../journey/round_11/README.md) · [Portal inputs/outputs for R11](../../data/portal_rounds_11_12.csv) · [Later reproducible DBSCAN diagnostic](../../research/diagnostics/clustering/clustering_audit.py) (the clustering study was contemporary; this script was assembled later and was not the original query generator) · [Later F1 reconstruction](../../src/bbo/f1_reconstruction.py) (retrospective numerical fit) · [Function-specific decision ledger](selection_history.csv).

</details>

<details>
<summary><strong>Round 12 · Controlled probes, repeats and structural investigations</strong> — 2.00000000</summary>

**Original learning context:** The same high-scoring coordinates were deliberately repeated, providing little new coverage.

**Strategy / candidate-selection evidence:** Controlled probes, repeats and structural investigations.

**Submitted input:** `0.628540-0.628540`  
**Actual portal result:** `1.9999999996761817`  
**Best observed before → after:** `1.9999999996761817` → `1.9999999996761817`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. The Week 13 reflection discussed allocating the final budget according to immediate benefit; the submitted point was a repeat of the R11 best.

**Supporting material:** [Round 12 evidence](../../journey/round_12/README.md) · [Dated Round 12 recommendations](../../journey/round_12/original/week12_full_review_2026-11-02.md) (documents the deliberate F1 repeat; the four original Week 12 analysis scripts did not separately generate this point) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 13 · Final decision</strong> — 2.00000000</summary>

**Original learning context:** The Week 13 reflection discussed allocating the final budget according to immediate benefit; the submitted point was a repeat of the R11 best.

**Strategy / candidate-selection evidence:** Final exploitation and regional probes.

**Submitted input:** `0.628540-0.628540`  
**Actual portal result:** `1.9999999996761817`  
**Best observed before → after:** `1.9999999996761817` → `1.9999999996761817`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. A weak GP on a numerically compressed target is a reason to challenge the representation, not endlessly tune one local model.

**Code and evidence:** [Round 13 reflection and portal evidence](../../journey/round_13/README.md) · [Submitted inputs](../../journey/round_13/queries.txt) · [Returned scores](../../journey/round_13/outputs.txt) · [Final thirteen-round reflection](../../journey/final_reflection/README.md) (final reasoning, not a surviving standalone selector) · [Function-specific decision ledger](selection_history.csv).

</details>

## Visual analysis

<table><tr><td width="50%"><img src="../../results/figures/f1_2d.svg" width="460" alt="Function 1 two-dimensional representation"></td><td width="50%"><img src="../../results/figures/f1_3d.svg" width="460" alt="Function 1 three-dimensional representation"></td></tr></table>

**Observed points only.** These 2D/3D views project the real inputs and their returned scores; no smooth objective surface has been invented. Both original input coordinates are displayed.

[How the visualisations were produced](../../docs/functions.md) · [Graph-generation code](../../results/figures/build_visual_gallery.mjs)

## Mathematical evidence and its limits

The recoverable model is the **two-component Gaussian-modulated cosine (Gabor-type) hypothesis**:

$$
\hat f_1(x_1,x_2)=\sum_{(c,A)\in\{(c_1,1),(c_2,2)\}} A\,e^{-1600[(x_1-c)^2+(x_2-c)^2]}\cos[40(x_1-c)]\cos[40(x_2-c)].
$$

Its centre coordinates are

$$
c_1=0.5-\frac{\pi}{40}\approx0.421460183660255,\qquad
c_2=0.55+\frac{\pi}{40}\approx0.628539816339745.
$$

| Coefficient | Value | Meaning |
|---|---:|---|
| Minor component amplitude | 1 | Smaller response region |
| Major component amplitude | 2 | Higher response region |
| Gaussian decay | 1600 | Rapid fall-off away from the centres |
| Cosine frequency | 40 | Oscillatory sign changes |
| Minor centre | 0.421460183660255 | Both inputs |
| Major centre | 0.628539816339745 | Both inputs |

**New retrospective validation, no peer observations:** [the executable fitting script](../../src/bbo/f1_reconstruction.py) fits these **six free parameters** using only the **10 course-supplied F1 observations in my dataset**, then evaluates **all 13 later personal portal results** without using those results for parameter fitting. The fit uses an **informed starting guess and an already proposed functional family**, not an uninformed discovery of a mathematical form. It reproduces the observations to approximately floating-point precision, including the zero return. [Automated regression tests](../../tests/test_f1_reconstruction.py) preserve the numerical check.

Run from the repository root after installing `requirements.txt`:

```bash
PYTHONPATH=src python -m bbo.f1_reconstruction
```

The returned Round 11 score at `[0.628540, 0.628540]` was **1.9999999996761817**. The reconstructed expression predicts the same value to the published precision. This is a **strong observational match**, not proof of identity with the undisclosed course source at every possible input, nor a certified global maximum on the full search domain.

The model family was available as a separate working implementation. **Its original derivation and authorship are not independently verified.** Historic Round 10–11 notes include earlier use of external exploratory evidence; these retrospective coefficient-fitting and validation tests **exclude all peer data** and do not rewrite the original chronology.

### Reconstructed function: modelled 2D/3D views

<table><tr><td width="50%"><img src="../../results/figures/f1_model_2d.svg" width="460" alt="Two-dimensional heatmap of F1 reconstructed model"></td><td width="50%"><img src="../../results/figures/f1_model_3d.svg" width="460" alt="Three-dimensional surface of F1 reconstructed model"></td></tr></table>

**Predicted values only:** these mathematical-model plots zoom to `0.32 ≤ x1,x2 ≤ 0.74` so both response regions are visible. The 3D camera has been rotated **45°** from the earlier view to separate the minor and major peaks on screen. They are **not additional portal measurements**. Compare with the observed-data plots immediately above. [Rebuild model figures](../../results/figures/build_f1_reconstruction.mjs) · [Reconstruction index](../../docs/reconstruction.md).

## Lessons to carry forward

A weak GP on a numerically compressed target is a reason to challenge the representation, not endlessly tune one local model.

**Source discipline:** The originally submitted weekly reflections informed the learning context; the portal results and preserved files establish what actually happened. Historical experiments, post-outcome explanations and model-generated graph values are not interchangeable.

[← All eight functions](../README.md) · [Dataset description](../../DATASHEET.md) · [Model card](../../MODEL_CARD.md)
