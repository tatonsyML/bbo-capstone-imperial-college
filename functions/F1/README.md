# Function 1 · Finding a signal in apparent numerical silence

[← All functions](../README.md) · [Project home](../../README.md) · [Observed inputs and outputs](observations.csv) · [Complete decision ledger](selection_history.csv)

**2 inputs · 10 starting observations · 13 rounds**

| Initial best | Final best | First achieved | Best input |
|---:|---:|:---:|---|
| `7.710875114502849e-16` | **`1.9999999996761817`** | **Round 11** | `0.628540-0.628540` |

## Understanding this function

Almost every early response was extremely close to zero. The first GP and UCB proposals could not locate a useful region, and local improvements around a weak incumbent were misleading. A later oscillatory, Gaussian-modulated structural reconstruction, informed by supplementary published evidence, guided Round 11 to almost 2. The reconstruction was checked numerically but its complete coefficients are not published here.

### Score progression from real evaluations

![Function 1 measured best-so-far history](progress.svg)

The chart tracks measured best-so-far results. A flat interval means no improvement to the incumbent, not that a model predicted a constant function.

## Weekly development · expand a round

Each round shows **what was known or being tested, what was submitted, what returned, and what was learnt**. The original 52-page weekly reflection is the narrative foundation; the decision ledger, surviving code and official portal records establish what was actually submitted. An exact historic kernel/seed/forecast appears only if retained. Where early rationale was reconstructed later, it is explicitly labelled in the ledger.

<details>
<summary><strong>Round 1 · Opening hypothesis</strong> — 0.00000000</summary>

**Original learning context:** The first reflection described F1 as nearly all zero and chose an under-sampled area because no useful local peak had been established.

**Strategy / candidate-selection evidence:** GP and acquisition baseline (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.02-0.98`  
**Actual portal result:** `0.0`  
**Best observed before → after:** `7.710875114502849e-16` → `7.710875114502849e-16`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Second round: GP/UCB with per-function exploration weights; deterministic candidate grids or pools.

**Supporting material:** [Round 1 evidence](../../journey/round_01/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 2 evidence](../../journey/round_02/README.md) · [Related surviving script/notebook](../../journey/round_02/week2_ucb_course_aligned.py) (related historical script not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 3 evidence](../../journey/round_03/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 4 evidence](../../journey/round_04/README.md) · [Related surviving script/notebook](../../journey/round_04/capstone_bbo_week4_module15.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 5 evidence](../../journey/round_05/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 6 evidence](../../journey/round_06/README.md) · [Related surviving script/notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) (related notebook original fitter missing, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 7 evidence](../../journey/round_07/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 8 evidence](../../journey/round_08/README.md) · [Related surviving script/notebook](../../journey/round_08/capstone_bbo_module19_round8.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 9 evidence](../../journey/round_09/README.md) · [Related surviving script/notebook](../../journey/round_09/round9_controlled_fits.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 10 evidence](../../journey/round_10/README.md) · [Related surviving script/notebook](../../src/bbo/optimizer.py) (related challenger not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 11 evidence](../../journey/round_11/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 12 evidence](../../journey/round_12/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

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

**Supporting material:** [Round 13 evidence](../../journey/round_13/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

## Visual analysis

<table><tr><td width="50%"><img src="../../results/figures/f1_2d.svg" width="460" alt="Function 1 two-dimensional representation"></td><td width="50%"><img src="../../results/figures/f1_3d.svg" width="460" alt="Function 1 three-dimensional representation"></td></tr></table>

**Observed points only.** These 2D/3D views project the real inputs and their returned scores; no smooth objective surface has been invented. Both original input coordinates are displayed.

[How the visualisations were produced](../../docs/functions.md) · [Graph-generation code](../../results/figures/build_visual_gallery.mjs)

## Mathematical evidence and its limits

The F1 structure was interpreted as a **two-component Gaussian-modulated oscillatory response**. A subsequently checked model agreed numerically with recorded samples and guided R11 towards **(0.628540, 0.628540)**, returning **1.9999999996761817**. It used supplementary evidence beyond personal portal queries. A [recovered October analytical script](../../journey/round_11/supplementary_analysis/bbo_clustering_audit.py) now records a fully parameterised hypothesis: 

$
\hat f_1(\mathbf x)=g(\mathbf x;0.5-\pi/40)+2g(\mathbf x;0.55+\pi/40),\quad g(\mathbf x;c)=e^{-1600\sum_i(x_i-c)^2}\prod_i\cos(40(x_i-c)).
$

This expression is supported by observations and supplementary information; it is **not** an authenticated copy of the hidden implementation, and the recovered script has not been verified byte-for-byte against the original raw file. The 2D/3D plots above continue to show **measured points only**, not an invented smooth surface.

## Lessons to carry forward

A weak GP on a numerically compressed target is a reason to challenge the representation, not endlessly tune one local model.

**Source discipline:** The originally submitted weekly reflections informed the learning context; the portal results and preserved files establish what actually happened. Historical experiments, post-outcome explanations and model-generated graph values are not interchangeable.

[← All eight functions](../README.md) · [Dataset description](../../DATASHEET.md) · [Model card](../../MODEL_CARD.md)
