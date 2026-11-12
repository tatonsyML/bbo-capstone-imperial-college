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

<details>
<summary><strong>Round 1 · Opening hypothesis</strong> — 1.36055550</summary>

**Reasoning:** The Week 1 reflection started from strong observed configurations but changed several coordinates to test whether the good region extended further.

**Approach:** GP and acquisition baseline.

**Submitted input:** `0.034737-0.246867-0.265123-0.307852-0.362506-0.937209`  
**Result:** `1.3605555033645358`  
**Best observed before → after:** `1.3649683044991994` → `1.3649683044991994`.

**What I learnt:** The submitted point did not beat the incumbent. Second round: GP/UCB with per-function exploration weights; deterministic candidate grids or pools.

**Code and results:** [Round 1 research](../../journey/round_01/README.md) · [Submitted inputs](../../journey/round_01/queries.txt) · [Returned scores](../../journey/round_01/outputs.txt) · [Original coursework notebook](../../journey/round_01/supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb) (coursework, not a verified portal generator) · No separate candidate-generator source authenticated · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 2 · GP and UCB working package</strong> — 1.02040228</summary>

**Reasoning:** After R1 returned 1.3606, only slightly below the original best, Week 2 used UCB κ=2.0 to balance exploration and exploitation.

**Approach:** GP and UCB working package.

**Submitted input:** `0.074002-0.315323-0.247287-0.026732-0.35885-0.832838`  
**Result:** `1.020402279048806`  
**Best observed before → after:** `1.3649683044991994` → `1.3649683044991994`.

**What I learnt:** The submitted point did not beat the incumbent. Original Week 3 methodology used a local EI approach as the signal became clearer.

**Code and results:** [Round 2 research](../../journey/round_02/README.md) · [Submitted inputs](../../journey/round_02/queries.txt) · [Returned scores](../../journey/round_02/outputs.txt) · [Original GP/UCB selection script](../../journey/round_02/week2_ucb_course_aligned.py) · [Eight saved selections](../../journey/round_02/week2_ucb_results.csv) (all eight saved portal values match the submitted record) · [Notebook](../../journey/round_02/Capstone_BBO_Week2_UCB_only.ipynb) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 3 · Function-specific EI or wider search</strong> — 1.61379630 ★ new best</summary>

**Reasoning:** Original Week 3 methodology used a local EI approach as the signal became clearer.

**Approach:** Function-specific EI or wider search.

**Submitted input:** `0.046316-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Result:** `1.6137963046751616`  
**Best observed before → after:** `1.3649683044991994` → `1.6137963046751616`.

**What I learnt:** The submitted point established a new personal best. The Week 4 reflection reported that neural-network gradients highlighted x1 and x6 as potentially influential, alongside SVM and GP challengers.

**Code and results:** [Round 3 research](../../journey/round_03/README.md) · [Submitted inputs](../../journey/round_03/queries.txt) · [Returned scores](../../journey/round_03/outputs.txt) · The original reflection records function-specific acquisition choices; no standalone original query generator is preserved for this round · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 4 · GP, SVM and neural-network diagnostics</strong> — 1.55163248</summary>

**Reasoning:** The Week 4 reflection reported that neural-network gradients highlighted x1 and x6 as potentially influential, alongside SVM and GP challengers.

**Approach:** GP, SVM and neural-network diagnostics.

**Submitted input:** `0.015-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Result:** `1.5516324818204723`  
**Best observed before → after:** `1.6137963046751616` → `1.6137963046751616`.

**What I learnt:** The submitted point did not beat the incumbent. The Week 6 reflection notes that increasing x1 through controlled values while holding x2–x6 fixed yielded a stable improving sequence.

**Code and results:** [Round 4 research](../../journey/round_04/README.md) · [Submitted inputs](../../journey/round_04/queries.txt) · [Returned scores](../../journey/round_04/outputs.txt) · [Original analysis code](../../journey/round_04/capstone_bbo_week4_module15.py) · [Executed notebook](../../journey/round_04/Capstone_BBO_Week4_Module15.ipynb) (final eight inputs stored explicitly; hybrid selection, not an autonomous selector) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 5 · Controlled coordinate probes</strong> — 1.63844015 ★ new best</summary>

**Reasoning:** The Week 6 reflection notes that increasing x1 through controlled values while holding x2–x6 fixed yielded a stable improving sequence.

**Approach:** Controlled coordinate probes.

**Submitted input:** `0.06-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Result:** `1.638440146032503`  
**Best observed before → after:** `1.6137963046751616` → `1.638440146032503`.

**What I learnt:** The submitted point established a new personal best. Five-fold cross-validation after R5 showed GP NRMSE 0.112 compared with 0.314 for the small MLP, supporting the simpler GP on F7.

**Code and results:** [Round 5 research](../../journey/round_05/README.md) · [Submitted inputs](../../journey/round_05/queries.txt) · [Returned scores](../../journey/round_05/outputs.txt) · Contemporary reflection and submitted measurements preserved; no standalone selection code authenticated · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 6 · GP, ridge and MLP comparison; controlled local fit</strong> — 1.70065969 ★ new best</summary>

**Reasoning:** Five-fold cross-validation after R5 showed GP NRMSE 0.112 compared with 0.314 for the small MLP, supporting the simpler GP on F7.

**Approach:** GP, ridge and MLP comparison; controlled local fit.

**Submitted input:** `0.1-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Result:** `1.7006596900158717`  
**Best observed before → after:** `1.638440146032503` → `1.7006596900158717`.

**What I learnt:** The submitted point established a new personal best. Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Code and results:** [Round 6 research](../../journey/round_06/README.md) · [Submitted inputs](../../journey/round_06/queries.txt) · [Returned scores](../../journey/round_06/outputs.txt) · [Original Module 17 notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) · [Eight selected inputs](../../journey/round_06/results/round6_queries.csv) · [Decision rationale](../../journey/round_06/results/round6_query_rationale.csv) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 7 · ARD and local forecast investigations</strong> — 1.75571821 ★ new best</summary>

**Reasoning:** Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Approach:** ARD and local forecast investigations.

**Submitted input:** `0.15-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Result:** `1.7557182120997592`  
**Best observed before → after:** `1.7006596900158717` → `1.7557182120997592`.

**What I learnt:** The submitted point established a new personal best. A one-dimensional quadratic through the x1 trajectory suggested a local vertex near 0.234, but this concerned only a restricted path.

**Code and results:** [Round 7 research](../../journey/round_07/README.md) · [Submitted inputs](../../journey/round_07/queries.txt) · [Returned scores](../../journey/round_07/outputs.txt) · [Week 7 forecast comparisons](../../journey/round_08/results/week7_audit.csv) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 8 · Testing the x1-path quadratic</strong> — 1.78586255 ★ new best</summary>

**Reasoning:** A one-dimensional quadratic through the x1 trajectory suggested a local vertex near 0.234, but this concerned only a restricted path.

**Approach:** The x1-only controlled path continues to fit a stable concave quadratic. The last three points place the estimated vertex at x1≈0.234070..

**Submitted input:** `0.23407-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Result:** `1.785862549726479`  
**Best observed before → after:** `1.7557182120997592` → `1.785862549726479`.

**Forecast preserved before the Round 8 return:** approximately `1.791396` (local quadratic; see [Round 8 forecast table](../../journey/round_08/README.md)).

**What I learnt:** The submitted point established a new personal best. The measured local progression began to flatten; further one-coordinate adjustments offered little upside.

**Code and results:** [Round 8 research](../../journey/round_08/README.md) · [Submitted inputs](../../journey/round_08/queries.txt) · [Returned scores](../../journey/round_08/outputs.txt) · [Original Module 19 Python analysis](../../journey/round_08/capstone_bbo_module19_round8.py) · [Original eight-input decision record](../../journey/round_08/results/round8_queries.csv) (all eight match portal inputs) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 9 · Refining the x1 local vertex</strong> — 1.78633820 ★ new best</summary>

**Reasoning:** The measured local progression began to flatten; further one-coordinate adjustments offered little upside.

**Approach:** The updated quadratic across the controlled x1 series places the local vertex near x1=0.228702, with only about 0.00055 predicted headroom. This is deliberate precision, not broad exploration..

**Submitted input:** `0.228702-0.36927-0.256273-0.262985-0.391467-0.834089`  
**Result:** `1.786338197796892`  
**Best observed before → after:** `1.785862549726479` → `1.786338197796892`.

**Pre-result numerical forecast:** `1.786415130748528` (recorded before return).

**What I learnt:** The submitted point established a new personal best. The original Round 10 plan explicitly stopped polishing the local vertex and proposed a different multi-coordinate region, whose expected mean was about 2.79 versus 1.73 locally.

**Code and results:** [Round 9 research](../../journey/round_09/README.md) · [Submitted inputs](../../journey/round_09/queries.txt) · [Returned scores](../../journey/round_09/outputs.txt) · [Dated eight-input decision and forecast ledger](../../journey/round_09/results/round9_queries.csv) (all eight match portal inputs) · [Original controlled local-fitting code](../../journey/round_09/round9_controlled_fits.py) (includes F7 analysis) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 10 · Alternative basin; peer-informed ensemble; substantial uncertainty</strong> — 3.14945880 ★ new best</summary>

**Reasoning:** The original Round 10 plan explicitly stopped polishing the local vertex and proposed a different multi-coordinate region, whose expected mean was about 2.79 versus 1.73 locally.

**Approach:** Alternative basin; peer-informed ensemble; substantial uncertainty.

**Submitted input:** `0.190478-0.171014-0.347582-0.283057-0.283946-0.639922`  
**Result:** `3.149458800087033`  
**Best observed before → after:** `1.786338197796892` → `3.149458800087033`.

**What I learnt:** The submitted point established a new personal best.

**Code and results:** [Round 10 research](../../journey/round_10/README.md) · [Submitted inputs](../../journey/round_10/queries.txt) · [Returned scores](../../journey/round_10/outputs.txt) · [Dated final candidate list](../../journey/round_10/round10_candidates.csv) · [Pre-result planning snapshot](../../journey/round_10/optimisation.yaml) · [GP/HEBO-inspired/TuRBO-style challenger code](../../src/bbo/optimizer.py) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 11 · Alternative-region exploration and structural investigations</strong> — 3.27896793 ★ new best</summary>

**Reasoning:** I tested another multi-coordinate region after the improvement in R10.

**Approach:** Alternative-region exploration and structural investigations.

**Submitted input:** `0.233000-0.128000-0.522000-0.276000-0.310000-0.667000`  
**Result:** `3.278967926227992`  
**Best observed before → after:** `3.149458800087033` → `3.278967926227992`.

**What I learnt:** The submitted point established a new personal best at 3.278968, encouraging further exploration of the new region.

**Code and results:** [Round 11 research](../../journey/round_11/README.md) · [Portal inputs/outputs for R11](../../data/portal_rounds_11_12.csv) · [Later reproducible DBSCAN diagnostic](../../research/diagnostics/clustering/clustering_audit.py) · [Later F7 Hartmann-6 validation](../../src/bbo/f7_reconstruction.py) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 12 · Controlled probes, repeats and structural investigations</strong> — 3.32236801 ★ new best</summary>

**Reasoning:** The Week 12 positive Hartmann-6 prospective forecast 3.32236801 matched the returned 3.322368011393.

**Approach:** Controlled probes, repeats and structural investigations.

**Submitted input:** `0.201689-0.150011-0.476874-0.275332-0.311652-0.657301`  
**Result:** `3.3223680113931557`  
**Best observed before → after:** `3.278967926227992` → `3.3223680113931557`.

**Pre-result numerical forecast:** `3.32236801` (approximate pre result forecast in round 12 notes).

**What I learnt:** The submitted point established a new personal best. A change of one millionth in x1 returned a marginally lower score; R12 remains the measured best.

**Supporting material:** [Round 12 evidence](../../journey/round_12/README.md) · [Dated Round 12 recommendations](../../journey/round_12/original/week12_full_review_2026-11-02.md) (records the Hartmann-6-based choice) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 13 · Final decision</strong> — 3.32236801</summary>

**Reasoning:** A change of one millionth in x1 returned a marginally lower score; R12 remains the measured best.

**Approach:** Final exploitation and regional probes.

**Submitted input:** `0.201690-0.150011-0.476874-0.275332-0.311652-0.657301`  
**Result:** `3.322368011392718`  
**Best observed before → after:** `3.3223680113931557` → `3.3223680113931557`.

**What I learnt:** The submitted point did not beat the incumbent. Controlled probes explain local coordinate effects, but alternative regions can dominate. A genuine pre-result structural prediction is more persuasive than post-hoc curve fitting.

**Code and results:** [Round 13 research](../../journey/round_13/README.md) · [Submitted inputs](../../journey/round_13/queries.txt) · [Returned scores](../../journey/round_13/outputs.txt) · [Final thirteen-round reflection](../../journey/final_reflection/README.md) (final reasoning, not a surviving standalone selector) · [Decision history](selection_history.csv).

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
