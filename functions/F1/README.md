# Function 1 · Finding a signal in apparent numerical silence

[← All functions](../README.md) · [Project home](../../README.md) · [Observed inputs and outputs](observations.csv) · [Complete decision ledger](selection_history.csv)

**2 inputs · 10 starting observations · 13 rounds**

| Initial best | Final best | First achieved | Best input |
|---:|---:|:---:|---|
| `7.710875114502849e-16` | **`1.9999999996761817`** | **Round 11** | `0.628540-0.628540` |

## Understanding this function

Almost every early response was extremely close to zero. The first GP and UCB proposals could not locate a useful region, and local improvements around a weak incumbent were misleading. A later mathematical reconstruction helps explain the sharp response pattern and is presented separately below.

### Score progression from real evaluations

![Function 1 measured best-so-far history](progress.svg)

The chart tracks measured best-so-far results. A flat interval means no improvement to the incumbent, not that a model predicted a constant function.

## Weekly development · expand a round

<details>
<summary><strong>Round 1 · Opening hypothesis</strong> — 0.00000000</summary>

**Why this input:** The first reflection described F1 as nearly all zero and chose an under-sampled area because no useful local peak had been established.

**Approach considered:** GP and acquisition baseline

**Submitted input:** `0.02-0.98`  
**Actual portal result:** `0.0`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**What I learnt:** The first exploratory point returned zero, leaving the already tiny initial best unchanged.

**Code and data:** [Round notes](../../journey/round_01/README.md) · [Inputs](../../journey/round_01/queries.txt) · [Outputs](../../journey/round_01/outputs.txt) · [Coursework notebook](../../journey/round_01/supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb).

</details>

<details>
<summary><strong>Round 2 · GP and UCB working package</strong> — -1.96324543e-233</summary>

**Why this input:** After the first query returned zero, the original Week 2 reflection gave F1 the largest UCB exploration weight, κ=3.0, and considered a future signal/no-signal classifier without claiming it was already implemented.

**Approach considered:** GP and UCB working package

**Submitted input:** `0.052001-0.865999`  
**Actual portal result:** `-1.9632454298284602e-233`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**What I learnt:** The uncertainty-led GP/UCB proposal still found no useful signal; a wider search alone did not resolve the near-zero response problem.

**Code and data:** [Round notes](../../journey/round_02/README.md) · [Inputs](../../journey/round_02/queries.txt) · [Outputs](../../journey/round_02/outputs.txt) · [GP/UCB Python code](../../journey/round_02/week2_ucb_course_aligned.py) · [Saved candidates](../../journey/round_02/week2_ucb_results.csv) · [Notebook](../../journey/round_02/Capstone_BBO_Week2_UCB_only.ipynb).

</details>

<details>
<summary><strong>Round 3 · Function-specific EI or wider search</strong> — 2.69213109e-65</summary>

**Why this input:** Third round: function-specific EI/UCB policy; 1%-of-output-SD EI margin and GP fitting restarts documented at pipeline level.

**Approach considered:** Function-specific EI or wider search

**Submitted input:** `0.636406-0.206433`  
**Actual portal result:** `2.69213108614911e-65`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**What I learnt:** The new response was negligible, so the search still lacked a promising high-scoring region.

**Code and data:** [Round notes](../../journey/round_03/README.md) · [Inputs](../../journey/round_03/queries.txt) · [Outputs](../../journey/round_03/outputs.txt).

</details>

<details>
<summary><strong>Round 4 · GP, SVM and neural-network diagnostics</strong> — 1.51764873e-192</summary>

**Why this input:** Fourth round: GP paired with SVM good/bad checks and small neural-network gradient challengers, not hard classifier exclusion.

**Approach considered:** GP, SVM and neural-network diagnostics

**Submitted input:** `0.999999-0.999999`  
**Actual portal result:** `1.517648729565899e-192`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**What I learnt:** The upper-corner test returned essentially zero; extreme coordinates were not a shortcut to a useful score.

**Code and data:** [Round notes](../../journey/round_04/README.md) · [Inputs](../../journey/round_04/queries.txt) · [Outputs](../../journey/round_04/outputs.txt) · [Python analysis](../../journey/round_04/capstone_bbo_week4_module15.py) · [Notebook](../../journey/round_04/Capstone_BBO_Week4_Module15.ipynb).

</details>

<details>
<summary><strong>Round 5 · Controlled coordinate probes</strong> — 1.33191455e-22</summary>

**Why this input:** Fifth round: use controlled coordinate differences to avoid confusing a multi-variable shift with a causal single-input effect.

**Approach considered:** Controlled coordinate probes

**Submitted input:** `0.75-0.75`  
**Actual portal result:** `1.3319145509281447e-22`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**What I learnt:** This controlled change did not reveal a useful new response region.

**Code and data:** [Round notes](../../journey/round_05/README.md) · [Inputs](../../journey/round_05/queries.txt) · [Outputs](../../journey/round_05/outputs.txt).

</details>

<details>
<summary><strong>Round 6 · GP, ridge and MLP comparison; controlled local fit</strong> — 3.25547512e-17</summary>

**Why this input:** Sixth round: compare GP and MLP using five-fold cross-validated error; treat extra model flexibility as something to justify.

**Approach considered:** GP, ridge and MLP comparison; controlled local fit

**Submitted input:** `0.732524-0.7389`  
**Actual portal result:** `3.2554751168755075e-17`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**What I learnt:** The alternative local comparison remained in an almost-zero area, showing why response scale mattered.

**Code and data:** [Round notes](../../journey/round_06/README.md) · [Inputs](../../journey/round_06/queries.txt) · [Outputs](../../journey/round_06/outputs.txt) · [Notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) · [Eight selected inputs](../../journey/round_06/results/round6_queries.csv) · [Decision notes](../../journey/round_06/results/round6_query_rationale.csv).

</details>

<details>
<summary><strong>Round 7 · ARD and local forecast investigations</strong> — 1.31425296e-15 ★ new best</summary>

**Why this input:** Near-zero results still held almost no meaningful signal; the Week 7 paper prioritised ARD kernels and checking how well forecasts survived the next portal return.

**Approach considered:** ARD and local forecast investigations

**Submitted input:** `0.730874-0.7318`  
**Actual portal result:** `1.3142529628112004e-15`  
**Best observed before → after:** `7.710875114502849e-16` → `1.3142529628112004e-15`.

**What I learnt:** This was technically a new best, but the value remained tiny; it was not yet a useful high-response region.

**Code and data:** [Round notes](../../journey/round_07/README.md) · [Inputs](../../journey/round_07/queries.txt) · [Outputs](../../journey/round_07/outputs.txt) · [Forecast comparison](../../journey/round_08/results/week7_audit.csv).

</details>

<details>
<summary><strong>Round 8 · Rank-GP exploration near the Round 7 incumbent</strong> — 4.19700395e-16</summary>

**Why this input:** Eighth round: separate LLM hypothesis generation from deterministic numerical validation and check candidate precision.

**Approach:** Rank-GP local consensus around the new Week 7 best; stay inside the near-zero basin while testing a small x1-up/x2-down move.

**Submitted input:** `0.735874-0.729467`  
**Actual portal result:** `4.1970039548686525e-16`  
**Best observed before → after:** `1.3142529628112004e-15` → `1.3142529628112004e-15`.

**What I learnt:** A small move near the incumbent reduced the response, giving little reason to keep polishing that neighbourhood.

**Code and data:** [Round notes](../../journey/round_08/README.md) · [Inputs](../../journey/round_08/queries.txt) · [Outputs](../../journey/round_08/outputs.txt) · [Python analysis](../../journey/round_08/capstone_bbo_module19_round8.py) · [Saved candidates](../../journey/round_08/results/round8_queries.csv).

</details>

<details>
<summary><strong>Round 9 · Single-coordinate test around the Round 7 best</strong> — 1.92128079e-15 ★ new best</summary>

**Why this input:** A cautious one-coordinate change was chosen while the output scale remained pathological; I had not yet located the main positive-response region.

**Approach:** One-coordinate probe: move x1 down by 0.001 from the Week 7 incumbent while holding x2 fixed. The updated rank-GP committee favours lower x1, but the output scale is too pathological for a trustworthy numeric forecast.

**Submitted input:** `0.729874-0.7318`  
**Actual portal result:** `1.921280788064022e-15`  
**Best observed before → after:** `1.3142529628112004e-15` → `1.921280788064022e-15`.

**What I learnt:** The score improved only at a negligible scale. The existing local region was not delivering meaningful progress.

**Code and data:** [Round notes](../../journey/round_09/README.md) · [Inputs](../../journey/round_09/queries.txt) · [Outputs](../../journey/round_09/outputs.txt) · [Candidate forecasts](../../journey/round_09/results/round9_queries.csv).

</details>

<details>
<summary><strong>Round 10 · Testing a different positive-response region</strong> — 0.00000726400118 ★ new best</summary>

**Why this input:** The repeated near-zero search had become unproductive. I tested a separate positive-response region rather than another tiny local adjustment.

**Approach:** Alternative-region search guided by a developing structural hypothesis.

**Submitted input:** `0.582552-0.558941`  
**Actual portal result:** `0.000007264001184177771`  
**Best observed before → after:** `1.921280788064022e-15` → `0.000007264001184177771`.

**What I learnt:** Testing another region produced a clear positive response, many orders of magnitude larger than the earlier values.

**Code and data:** [Round notes](../../journey/round_10/README.md) · [Inputs](../../journey/round_10/queries.txt) · [Outputs](../../journey/round_10/outputs.txt) · [Candidate list](../../journey/round_10/round10_candidates.csv) · [Search plan](../../journey/round_10/optimisation.yaml) · [Related optimiser code](../../src/bbo/optimizer.py).

</details>

<details>
<summary><strong>Round 11 · Finding a high-scoring point</strong> — 2.00000000 ★ new best</summary>

**Why this input:** Round 10 revealed a positive-response region. I tested a different nearby point under a Gaussian-modulated structural hypothesis.

**Approach:** Testing a higher-response region.

**Submitted input:** `0.628540-0.628540`  
**Actual portal result:** `1.9999999996761817`  
**Best observed before → after:** `0.000007264001184177771` → `1.9999999996761817`.

**What I learnt:** The alternative-region input returned almost 2, the first substantial high-response result of the search.

**Code and data:** [Round notes](../../journey/round_11/README.md) · [Portal results](../../data/portal_rounds_11_12.csv) · [Clustering analysis (later reproduction)](../../research/diagnostics/clustering/clustering_audit.py) · [F1 mathematical model (later)](../../src/bbo/f1_reconstruction.py).

</details>

<details>
<summary><strong>Round 12 · Repeating the strongest result</strong> — 2.00000000</summary>

**Why this input:** After Round 11 returned almost 2, I repeated its exact coordinates to test consistency.

**Approach:** Repeat query for consistency.

**Submitted input:** `0.628540-0.628540`  
**Actual portal result:** `1.9999999996761817`  
**Best observed before → after:** `1.9999999996761817` → `1.9999999996761817`.

**What I learnt:** Repeating the high-scoring vector returned the same value. This checked consistency without adding a new location.

**Code and data:** [Round 12 evidence](../../journey/round_12/README.md) · [Candidate rationale](../../journey/round_12/original/week12_full_review_2026-11-02.md) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 13 · Final repeat at the best point</strong> — 2.00000000</summary>

**Why this input:** The same high-scoring coordinates had succeeded twice, so I used the final query for another consistency check.

**Approach:** Final repeat at the observed best.

**Submitted input:** `0.628540-0.628540`  
**Actual portal result:** `1.9999999996761817`  
**Best observed before → after:** `1.9999999996761817` → `1.9999999996761817`.

**What I learnt:** The final repeat confirmed consistency at the successful point, not broader coverage of the input space.

**Code and data:** [Round notes](../../journey/round_13/README.md) · [Inputs](../../journey/round_13/queries.txt) · [Outputs](../../journey/round_13/outputs.txt) · [Final reflection](../../journey/final_reflection/README.md).

</details>

## Visual analysis

<table><tr><td width="50%"><img src="../../results/figures/f1_2d.svg" width="460" alt="Function 1 two-dimensional representation"></td><td width="50%"><img src="../../results/figures/f1_3d.svg" width="460" alt="Function 1 three-dimensional representation"></td></tr></table>

**Observed points only.** These 2D/3D views project the real inputs and their returned scores; no smooth objective surface has been invented. Both original input coordinates are displayed.

[How the visualisations were produced](../../docs/functions.md) · [Graph-generation code](../../results/figures/build_visual_gallery.mjs)

## Mathematical evidence and its limits

The reconstructed model is the **two-component Gaussian-modulated cosine (Gabor-type) hypothesis**:

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


[← All eight functions](../README.md) · [Dataset description](../../DATASHEET.md) · [Model card](../../MODEL_CARD.md)
