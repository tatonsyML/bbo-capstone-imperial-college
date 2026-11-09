# Function 7 · From one-coordinate refinement to structural prediction

[← All functions](../README.md) · [Project home](../../README.md) · [Observed inputs and outputs](observations.csv) · [Complete decision ledger](selection_history.csv)

**6 inputs · 30 starting observations · 13 rounds**

| Initial best | Final best | First achieved | Best input |
|---:|---:|:---:|---|
| `1.3649683044991994` | **`3.3223680113931557`** | **Round 12** | `0.201689-0.150011-0.476874-0.275332-0.311652-0.657301` |

## Understanding this function

F7 initially rewarded a controlled one-coordinate path, with x1 changes improving a local best to 1.786338 by R9. Moving to a different multi-coordinate region in R10 produced 3.149459. A positive Hartmann-6 reconstruction then forecast 3.32236801 *before* R12, which the portal confirmed to high precision. This is strong tested evidence, not authentication of the undisclosed function everywhere.

### Score progression from real evaluations

![Function 7 measured best-so-far history](progress.svg)

The chart tracks measured best-so-far results. A flat interval means no improvement to the incumbent, not that a model predicted a constant function.

## Weekly development · expand a round

Each round shows **what was known or being tested, what was submitted, what returned, and what was learnt**. The original 52-page weekly reflection is the narrative foundation; the decision ledger, surviving code and official portal records establish what was actually submitted. An exact historic kernel/seed/forecast appears only if retained. Where early rationale was reconstructed later, it is explicitly labelled in the ledger.

<details>
<summary><strong>Round 1 · Opening hypothesis</strong> — 1.36055550</summary>

**Original learning context:** The Week 1 reflection started from strong observed configurations but changed several coordinates to test whether the good region extended further.

**Strategy / candidate-selection evidence:** GP and acquisition baseline (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.034737-0.246867-0.265123-0.307852-0.362506-0.937209`  
**Actual portal result:** `1.3605555033645358`  
**Best observed before → after:** `1.3649683044991994` → `1.3649683044991994`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Second round: GP/UCB with per-function exploration weights; deterministic candidate grids or pools.

**Supporting material:** [Round 1 evidence](../../journey/round_01/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 2 · GP and UCB working package</strong> — 1.02040228</summary>

**Original learning context:** After R1 returned 1.3606, only slightly below the original best, Week 2 used UCB κ=2.0 to balance exploration and exploitation.

**Strategy / candidate-selection evidence:** GP and UCB working package *(early-round attribution partly retrospective)*.

**Submitted input:** `0.074002-0.315323-0.247287-0.026732-0.35885-0.832838`  
**Actual portal result:** `1.020402279048806`  
**Best observed before → after:** `1.3649683044991994` → `1.3649683044991994`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Original Week 3 methodology used a local EI approach as the signal became clearer.

**Supporting material:** [Round 2 evidence](../../journey/round_02/README.md) · [Related surviving script/notebook](../../journey/round_02/week2_ucb_course_aligned.py) (related historical script not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 3 · Function-specific EI or wider search (retrospective)</strong> — 1.61379630 ★ new best</summary>

**Original learning context:** Original Week 3 methodology used a local EI approach as the signal became clearer.

**Strategy / candidate-selection evidence:** Function-specific EI or wider search (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.046316-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Actual portal result:** `1.6137963046751616`  
**Best observed before → after:** `1.3649683044991994` → `1.6137963046751616`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The Week 4 reflection reported that neural-network gradients highlighted x1 and x6 as potentially influential, alongside SVM and GP challengers.

**Supporting material:** [Round 3 evidence](../../journey/round_03/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 4 · GP, SVM and neural-network diagnostics</strong> — 1.55163248</summary>

**Original learning context:** The Week 4 reflection reported that neural-network gradients highlighted x1 and x6 as potentially influential, alongside SVM and GP challengers.

**Strategy / candidate-selection evidence:** GP, SVM and neural-network diagnostics *(early-round attribution partly retrospective)*.

**Submitted input:** `0.015-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Actual portal result:** `1.5516324818204723`  
**Best observed before → after:** `1.6137963046751616` → `1.6137963046751616`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. The Week 6 reflection notes that increasing x1 through controlled values while holding x2–x6 fixed yielded a stable improving sequence.

**Supporting material:** [Round 4 evidence](../../journey/round_04/README.md) · [Related surviving script/notebook](../../journey/round_04/capstone_bbo_week4_module15.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 5 · Controlled coordinate probes (retrospective)</strong> — 1.63844015 ★ new best</summary>

**Original learning context:** The Week 6 reflection notes that increasing x1 through controlled values while holding x2–x6 fixed yielded a stable improving sequence.

**Strategy / candidate-selection evidence:** Controlled coordinate probes (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.06-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Actual portal result:** `1.638440146032503`  
**Best observed before → after:** `1.6137963046751616` → `1.638440146032503`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. Five-fold cross-validation after R5 showed GP NRMSE 0.112 compared with 0.314 for the small MLP, supporting the simpler GP on F7.

**Supporting material:** [Round 5 evidence](../../journey/round_05/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 6 · GP, ridge and MLP comparison; controlled local fit</strong> — 1.70065969 ★ new best</summary>

**Original learning context:** Five-fold cross-validation after R5 showed GP NRMSE 0.112 compared with 0.314 for the small MLP, supporting the simpler GP on F7.

**Strategy / candidate-selection evidence:** GP, ridge and MLP comparison; controlled local fit *(early-round attribution partly retrospective)*.

**Submitted input:** `0.1-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Actual portal result:** `1.7006596900158717`  
**Best observed before → after:** `1.638440146032503` → `1.7006596900158717`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Supporting material:** [Round 6 evidence](../../journey/round_06/README.md) · [Related surviving script/notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) (related notebook original fitter missing, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 7 · ARD and local forecast investigations (retrospective)</strong> — 1.75571821 ★ new best</summary>

**Original learning context:** Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Strategy / candidate-selection evidence:** ARD and local forecast investigations (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.15-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Actual portal result:** `1.7557182120997592`  
**Best observed before → after:** `1.7006596900158717` → `1.7557182120997592`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. A one-dimensional quadratic through the x1 trajectory suggested a local vertex near 0.234, but this concerned only a restricted path.

**Supporting material:** [Round 7 evidence](../../journey/round_07/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 8 · The x1-only controlled path continues to fit a stable concave quadratic. The…</strong> — 1.78586255 ★ new best</summary>

**Original learning context:** A one-dimensional quadratic through the x1 trajectory suggested a local vertex near 0.234, but this concerned only a restricted path.

**Strategy / candidate-selection evidence:** The x1-only controlled path continues to fit a stable concave quadratic. The last three points place the estimated vertex at x1≈0.234070..

**Submitted input:** `0.23407-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Actual portal result:** `1.785862549726479`  
**Best observed before → after:** `1.7557182120997592` → `1.785862549726479`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The measured local progression began to flatten; further one-coordinate adjustments offered little upside.

**Supporting material:** [Round 8 evidence](../../journey/round_08/README.md) · [Related surviving script/notebook](../../journey/round_08/capstone_bbo_module19_round8.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 9 · The updated quadratic across the controlled x1 series places the local verte…</strong> — 1.78633820 ★ new best</summary>

**Original learning context:** The measured local progression began to flatten; further one-coordinate adjustments offered little upside.

**Strategy / candidate-selection evidence:** The updated quadratic across the controlled x1 series places the local vertex near x1=0.228702, with only about 0.00055 predicted headroom. This is deliberate precision, not broad exploration..

**Submitted input:** `0.228702-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Actual portal result:** `1.786338197796892`  
**Best observed before → after:** `1.785862549726479` → `1.786338197796892`.

**Pre-result numerical forecast:** `1.786415130748528` (recorded before return).

**After the result:** The submitted point established a new personal best. The original Round 10 plan explicitly stopped polishing the local vertex and proposed a different multi-coordinate region, whose expected mean was about 2.79 versus 1.73 locally.

**Supporting material:** [Round 9 evidence](../../journey/round_09/README.md) · [Related surviving script/notebook](../../journey/round_09/round9_controlled_fits.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 10 · Alternative basin; peer-informed ensemble; substantial uncertainty</strong> — 3.14945880 ★ new best</summary>

**Original learning context:** The original Round 10 plan explicitly stopped polishing the local vertex and proposed a different multi-coordinate region, whose expected mean was about 2.79 versus 1.73 locally.

**Strategy / candidate-selection evidence:** Alternative basin; peer-informed ensemble; substantial uncertainty.

**Submitted input:** `0.190478-0.171014-0.347582-0.283057-0.283946-0.639922`  
**Actual portal result:** `3.149458800087033`  
**Best observed before → after:** `1.786338197796892` → `3.149458800087033`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The official Week 11 email confirms x=(0.233,0.128,0.522,0.276,0.310,0.667) and a returned 3.278967926227992; the original selection script is not available.

**Supporting material:** [Round 10 evidence](../../journey/round_10/README.md) · [Related surviving script/notebook](../../src/bbo/optimizer.py) (related challenger not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 11 · Alternative-region exploration and structural investigations</strong> — 3.27896793 ★ new best</summary>

**Original learning context:** The official Week 11 email confirms x=(0.233,0.128,0.522,0.276,0.310,0.667) and a returned 3.278967926227992; the original selection script is not available.

**Strategy / candidate-selection evidence:** Alternative-region exploration and structural investigations.

**Submitted input:** `0.233000-0.128000-0.522000-0.276000-0.310000-0.667000`  
**Actual portal result:** `3.278967926227992`  
**Best observed before → after:** `3.149458800087033` → `3.278967926227992`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The Week 12 positive Hartmann-6 prospective forecast 3.32236801 matched the returned 3.322368011393.

**Supporting material:** [Round 11 evidence](../../journey/round_11/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 12 · Controlled probes, repeats and structural investigations</strong> — 3.32236801 ★ new best</summary>

**Original learning context:** The Week 12 positive Hartmann-6 prospective forecast 3.32236801 matched the returned 3.322368011393.

**Strategy / candidate-selection evidence:** Controlled probes, repeats and structural investigations.

**Submitted input:** `0.201689-0.150011-0.476874-0.275332-0.311652-0.657301`  
**Actual portal result:** `3.3223680113931557`  
**Best observed before → after:** `3.278967926227992` → `3.3223680113931557`.

**Pre-result numerical forecast:** `3.32236801` (approximate pre result forecast in round 12 notes).

**After the result:** The submitted point established a new personal best. A change of one millionth in x1 returned a marginally lower score; R12 remains the measured best.

**Supporting material:** [Round 12 evidence](../../journey/round_12/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 13 · Final decision</strong> — 3.32236801</summary>

**Original learning context:** A change of one millionth in x1 returned a marginally lower score; R12 remains the measured best.

**Strategy / candidate-selection evidence:** Final exploitation and regional probes.

**Submitted input:** `0.201690-0.150011-0.476874-0.275332-0.311652-0.657301`  
**Actual portal result:** `3.322368011392718`  
**Best observed before → after:** `3.3223680113931557` → `3.3223680113931557`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Controlled probes explain local coordinate effects, but alternative regions can dominate. A genuine pre-result structural prediction is more persuasive than post-hoc curve fitting.

**Supporting material:** [Round 13 evidence](../../journey/round_13/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

## Visual analysis

<table><tr><td width="50%"><img src="../../results/figures/f7_2d.svg" width="460" alt="Function 7 two-dimensional representation"></td><td width="50%"><img src="../../results/figures/f7_3d.svg" width="460" alt="Function 7 three-dimensional representation"></td></tr></table>

**Positive Hartmann-6 model slices:** vary x1 and x2 while **x3=0.476874, x4=0.275332, x5=0.311652 and x6=0.657301** remain fixed. The resulting surface is a model reconstruction, not a new set of portal observations.

[How the visualisations were produced](../../docs/functions.md) · [Graph-generation code](../../results/figures/build_visual_gallery.mjs)

## Mathematical evidence and its limits

The tested candidate was based on the **positive Hartmann-6** benchmark response (the sign-reversed form of the standard minimisation example). A **pre-result** forecast for R12 was **3.32236801**; the portal returned **3.3223680113931557**. The Round 13 change of x1 by one millionth returned **3.322368011392718**, marginally worse. [Benchmark definition](https://www.sfu.ca/~ssurjano/hart6.html) · [Implementation of the plotted form](../../results/figures/build_visual_gallery.mjs).

The matching tested outputs support the reconstructed family but do not establish identity at all untested six-dimensional inputs.

## Lessons to carry forward

Controlled probes explain local coordinate effects, but alternative regions can dominate. A genuine pre-result structural prediction is more persuasive than post-hoc curve fitting.

**Source discipline:** The originally submitted weekly reflections informed the learning context; the portal results and preserved files establish what actually happened. Historical experiments, post-outcome explanations and model-generated graph values are not interchangeable.

[← All eight functions](../README.md) · [Dataset description](../../DATASHEET.md) · [Model card](../../MODEL_CARD.md)
