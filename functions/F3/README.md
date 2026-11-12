# Function 3 · Learning when a fitted local peak is misleading

[← All functions](../README.md) · [Project home](../../README.md) · [Observed inputs and outputs](observations.csv) · [Complete decision ledger](selection_history.csv)

**3 inputs · 15 starting observations · 13 rounds**

| Initial best | Final best | First achieved | Best input |
|---:|---:|:---:|---|
| `-0.034835313350078584` | **`-0.0037530969187192596`** | **Round 13** | `0.197280-0.523429-0.470094` |

## Understanding this function

The response is negative, so higher (closer to zero) is better. Local searches found partial gains but repeatedly failed to generalise. Alternative regional inputs in R10/R11 and again in R13 improved the best substantially. No underlying analytical formula was established.

### Score progression from real evaluations

![Function 3 measured best-so-far history](progress.svg)

The chart tracks measured best-so-far results. A flat interval means no improvement to the incumbent, not that a model predicted a constant function.

## Weekly development · expand a round

<details>
<summary><strong>Round 1 · Opening hypothesis</strong> — -0.0437772385</summary>

**Reasoning:** The original first reflection noted that the best outputs were already close to zero and favoured cautious exploitation while retaining a promising coordinate.

**Approach:** GP and acquisition baseline.

**Submitted input:** `0.5-0.5-0.345`  
**Result:** `-0.0437772384849064`  
**Best observed before → after:** `-0.034835313350078584` → `-0.034835313350078584`.

**What I learnt:** The submitted point did not beat the incumbent. Second round: GP/UCB with per-function exploration weights; deterministic candidate grids or pools.

**Code and results:** [Round 1 research](../../journey/round_01/README.md) · [Submitted inputs](../../journey/round_01/queries.txt) · [Returned scores](../../journey/round_01/outputs.txt) · [Original coursework notebook](../../journey/round_01/supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb) (coursework, not a verified portal generator) · No separate candidate-generator source authenticated · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 2 · GP and UCB working package</strong> — -0.106495098</summary>

**Reasoning:** The first return was close to, but worse than, the starting best; Week 2 used a balanced UCB setting κ=2.0.

**Approach:** GP and UCB working package.

**Submitted input:** `0.993188-0.591985-0.00028`  
**Result:** `-0.1064950977729621`  
**Best observed before → after:** `-0.034835313350078584` → `-0.034835313350078584`.

**What I learnt:** The submitted point did not beat the incumbent. The Week 3 plan explicitly selected local predicted-mean optimisation for F3, not the globally exploratory EI used for F2.

**Code and results:** [Round 2 research](../../journey/round_02/README.md) · [Submitted inputs](../../journey/round_02/queries.txt) · [Returned scores](../../journey/round_02/outputs.txt) · [Original GP/UCB selection script](../../journey/round_02/week2_ucb_course_aligned.py) · [Eight saved selections](../../journey/round_02/week2_ucb_results.csv) (all eight saved portal values match the submitted record) · [Notebook](../../journey/round_02/Capstone_BBO_Week2_UCB_only.ipynb) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 3 · Function-specific EI or wider search</strong> — -0.0427365724</summary>

**Reasoning:** The Week 3 plan explicitly selected local predicted-mean optimisation for F3, not the globally exploratory EI used for F2.

**Approach:** Function-specific EI or wider search.

**Submitted input:** `0.496377-0.564413-0.34369`  
**Result:** `-0.0427365723752823`  
**Best observed before → after:** `-0.034835313350078584` → `-0.034835313350078584`.

**What I learnt:** The submitted point did not beat the incumbent. After the model comparison, the original reflection noted new records in F3 among others, supporting GP-led adaptation with SVM checks as secondary evidence.

**Code and results:** [Round 3 research](../../journey/round_03/README.md) · [Submitted inputs](../../journey/round_03/queries.txt) · [Returned scores](../../journey/round_03/outputs.txt) · The original reflection records function-specific acquisition choices; no standalone original query generator is preserved for this round · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 4 · GP, SVM and neural-network diagnostics</strong> — -0.0312815968 ★ new best</summary>

**Reasoning:** After the model comparison, the original reflection noted new records in F3 among others, supporting GP-led adaptation with SVM checks as secondary evidence.

**Approach:** GP, SVM and neural-network diagnostics.

**Submitted input:** `0.49-0.62-0.36`  
**Result:** `-0.0312815968234451`  
**Best observed before → after:** `-0.034835313350078584` → `-0.0312815968234451`.

**What I learnt:** The submitted point established a new personal best. Fifth round: use controlled coordinate differences to avoid confusing a multi-variable shift with a causal single-input effect.

**Code and results:** [Round 4 research](../../journey/round_04/README.md) · [Submitted inputs](../../journey/round_04/queries.txt) · [Returned scores](../../journey/round_04/outputs.txt) · [Original analysis code](../../journey/round_04/capstone_bbo_week4_module15.py) · [Executed notebook](../../journey/round_04/Capstone_BBO_Week4_Module15.ipynb) (final eight inputs stored explicitly; hybrid selection, not an autonomous selector) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 5 · Controlled coordinate probes</strong> — -0.0334231088</summary>

**Reasoning:** Fifth round: use controlled coordinate differences to avoid confusing a multi-variable shift with a causal single-input effect.

**Approach:** Controlled coordinate probes.

**Submitted input:** `0.483623-0.675587-0.37631`  
**Result:** `-0.0334231088352711`  
**Best observed before → after:** `-0.0312815968234451` → `-0.0312815968234451`.

**What I learnt:** The submitted point did not beat the incumbent. Original five-fold validation found that a small MLP slightly outperformed the GP on F3, unlike F7/F8. This challenged uncritical model preference.

**Code and results:** [Round 5 research](../../journey/round_05/README.md) · [Submitted inputs](../../journey/round_05/queries.txt) · [Returned scores](../../journey/round_05/outputs.txt) · Contemporary reflection and submitted measurements preserved; no standalone selection code authenticated · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 6 · GP, ridge and MLP comparison; controlled local fit</strong> — -0.0208561545 ★ new best</summary>

**Reasoning:** Original five-fold validation found that a small MLP slightly outperformed the GP on F3, unlike F7/F8. This challenged uncritical model preference.

**Approach:** GP, ridge and MLP comparison; controlled local fit.

**Submitted input:** `0.487816-0.639038-0.365586`  
**Result:** `-0.0208561545295093`  
**Best observed before → after:** `-0.0312815968234451` → `-0.0208561545295093`.

**What I learnt:** The submitted point established a new personal best. Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Code and results:** [Round 6 research](../../journey/round_06/README.md) · [Submitted inputs](../../journey/round_06/queries.txt) · [Returned scores](../../journey/round_06/outputs.txt) · [Original Module 17 notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) · [Eight selected inputs](../../journey/round_06/results/round6_queries.csv) · [Decision rationale](../../journey/round_06/results/round6_query_rationale.csv) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 7 · ARD and local forecast investigations</strong> — -0.0279111486</summary>

**Reasoning:** Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Approach:** ARD and local forecast investigations.

**Submitted input:** `0.486949-0.646592-0.367803`  
**Result:** `-0.0279111486430777`  
**Best observed before → after:** `-0.0208561545295093` → `-0.0208561545295093`.

**What I learnt:** The submitted point did not beat the incumbent. The original Week 8 reflection reported a failed F3 local prediction and increased emphasis on pre-recorded forecasts and numerical checks.

**Code and results:** [Round 7 research](../../journey/round_07/README.md) · [Submitted inputs](../../journey/round_07/queries.txt) · [Returned scores](../../journey/round_07/outputs.txt) · [Week 7 forecast comparisons](../../journey/round_08/results/week7_audit.csv) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 8 · Testing the local quadratic after an overshoot</strong> — -0.0296632774</summary>

**Reasoning:** The original Week 8 reflection reported a failed F3 local prediction and increased emphasis on pre-recorded forecasts and numerical checks.

**Approach:** Week 7 overshot the Week 6 local best. A quadratic through the left bracket, Week 6 best and Week 7 point places the local vertex back at t≈0.260 on the controlled path..

**Submitted input:** `0.488344-0.634434-0.364235`  
**Result:** `-0.0296632773887996`  
**Best observed before → after:** `-0.0208561545295093` → `-0.0208561545295093`.

**Forecast preserved before the Round 8 return:** approximately `−0.019675` (local-path model; see [Round 8 forecast table](../../journey/round_08/README.md)).

**What I learnt:** The submitted point did not beat the incumbent. The original Week 9 reflection warned that an optimistic F3 forecast near -0.01968 had returned around -0.02966.

**Code and results:** [Round 8 research](../../journey/round_08/README.md) · [Submitted inputs](../../journey/round_08/queries.txt) · [Returned scores](../../journey/round_08/outputs.txt) · [Original Module 19 Python analysis](../../journey/round_08/capstone_bbo_module19_round8.py) · [Original eight-input decision record](../../journey/round_08/results/round8_queries.csv) (all eight match portal inputs) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 9 · Updating the local-path quadratic</strong> — -0.0258164064</summary>

**Reasoning:** The original Week 9 reflection warned that an optimistic F3 forecast near -0.01968 had returned around -0.02966.

**Approach:** Updated local-path quadratic using Week 8, Week 6 and Week 7 places the vertex near this point, predicting about -0.02011. This is a tighter bracket after two forecast misses..

**Submitted input:** `0.487611-0.640821-0.366109`  
**Result:** `-0.0258164064206346`  
**Best observed before → after:** `-0.0208561545295093` → `-0.0208561545295093`.

**Pre-result numerical forecast:** `-0.02011192237870145` (recorded before return).

**What I learnt:** The submitted point did not beat the incumbent. The Week 10 submission describes rejecting a speculative restart in favour of an alternative x3 region, partly informed by separately attributed external data.

**Code and results:** [Round 9 research](../../journey/round_09/README.md) · [Submitted inputs](../../journey/round_09/queries.txt) · [Returned scores](../../journey/round_09/outputs.txt) · [Dated eight-input decision and forecast ledger](../../journey/round_09/results/round9_queries.csv) (all eight match portal inputs) · [Original controlled local-fitting code](../../journey/round_09/round9_controlled_fits.py) (includes F3 analysis) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 10 · Alternative-region local interpolation; external evidence; uncertain</strong> — -0.0146028106 ★ new best</summary>

**Reasoning:** The Week 10 submission describes rejecting a speculative restart in favour of an alternative x3 region, partly informed by separately attributed external data.

**Approach:** Alternative-region local interpolation; external evidence; uncertain.

**Submitted input:** `0.469634-0.620072-0.416672`  
**Result:** `-0.014602810625106634`  
**Best observed before → after:** `-0.0208561545295093` → `-0.014602810625106634`.

**What I learnt:** The submitted point established a new personal best. Eleventh round: analyse density with DBSCAN but do not confuse sampled clusters with high-performing regions.

**Code and results:** [Round 10 research](../../journey/round_10/README.md) · [Submitted inputs](../../journey/round_10/queries.txt) · [Returned scores](../../journey/round_10/outputs.txt) · [Dated final candidate list](../../journey/round_10/round10_candidates.csv) · [Pre-result planning snapshot](../../journey/round_10/optimisation.yaml) · [GP/HEBO-inspired/TuRBO-style challenger code](../../src/bbo/optimizer.py) (not proof of the exact final per-function generator) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 11 · Alternative-region exploration and structural investigations</strong> — -0.00570922028 ★ new best</summary>

**Reasoning:** Eleventh round: analyse density with DBSCAN but do not confuse sampled clusters with high-performing regions.

**Approach:** Alternative-region exploration and structural investigations.

**Submitted input:** `0.445500-0.593000-0.420000`  
**Result:** `-0.005709220275560069`  
**Best observed before → after:** `-0.014602810625106634` → `-0.005709220275560069`.

**What I learnt:** The submitted point established a new personal best. The R12 candidate returned a worse value than the R11 incumbent, showing that a wider search also incurs cost.

**Code and results:** [Round 11 research](../../journey/round_11/README.md) · [Portal inputs/outputs for R11](../../data/portal_rounds_11_12.csv) · [Later reproducible DBSCAN diagnostic](../../research/diagnostics/clustering/clustering_audit.py) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 12 · Controlled probes, repeats and structural investigations</strong> — -0.0226526646</summary>

**Reasoning:** The R12 candidate returned a worse value than the R11 incumbent, showing that a wider search also incurs cost.

**Approach:** Controlled probes, repeats and structural investigations.

**Submitted input:** `0.313581-0.474345-0.485191`  
**Result:** `-0.0226526646178297`  
**Best observed before → after:** `-0.005709220275560069` → `-0.005709220275560069`.

**What I learnt:** The submitted point did not beat the incumbent. With only one evaluation left, the selected regional input delivered the best of -0.003753; no claim of achieving zero is justified.

**Supporting material:** [Round 12 evidence](../../journey/round_12/README.md) · [Original Round 12 model and candidate-selection code](../../journey/round_12/original/review_round12.py) · [Original TPE and local-model comparisons](../../journey/round_12/original/tpe_local.py) · [Dated candidate rationale](../../journey/round_12/original/week12_full_review_2026-11-02.md) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 13 · Final decision</strong> — -0.00375309692 ★ new best</summary>

**Reasoning:** With only one evaluation left, the selected regional input delivered the best of -0.003753; no claim of achieving zero is justified.

**Approach:** Final exploitation and regional probes.

**Submitted input:** `0.197280-0.523429-0.470094`  
**Result:** `-0.0037530969187192596`  
**Best observed before → after:** `-0.005709220275560069` → `-0.0037530969187192596`.

**What I learnt:** The submitted point established a new personal best. A smooth local curve and an accurate-looking mean can still select an unproductive region. Holdout evidence and alternative basins matter.

**Code and results:** [Round 13 research](../../journey/round_13/README.md) · [Submitted inputs](../../journey/round_13/queries.txt) · [Returned scores](../../journey/round_13/outputs.txt) · [Final thirteen-round reflection](../../journey/final_reflection/README.md) (final reasoning, not a surviving standalone selector) · [Decision history](selection_history.csv).

</details>

## Visual analysis

<table><tr><td width="50%"><img src="../../results/figures/f3_2d.svg" width="460" alt="Function 3 two-dimensional representation"></td><td width="50%"><img src="../../results/figures/f3_3d.svg" width="460" alt="Function 3 three-dimensional representation"></td></tr></table>

**Observed points only.** These 2D/3D views project the real inputs and their returned scores; no smooth objective surface has been invented. Only x1 and x2 appear on the horizontal axes; x3 varies across observations and the plots do not control for them.

[How the visualisations were produced](../../docs/functions.md) · [Graph-generation code](../../results/figures/build_visual_gallery.mjs)

## Mathematical evidence and its limits

**No validated hidden-function equation is available.** RBF and Matérn GPs, local fits and neural-network challengers are approximate predictive tools, not claims to know the underlying source. The observed maximum in the table is **a personal best**, not a proved global optimum.

## Lessons to carry forward

A smooth local curve and an accurate-looking mean can still select an unproductive region. Holdout evidence and alternative basins matter.

**Source discipline:** The originally submitted weekly reflections informed the learning context; the portal results and preserved files establish what actually happened. Historical experiments, post-outcome explanations and model-generated graph values are not interchangeable.

[← All eight functions](../README.md) · [Dataset description](../../DATASHEET.md) · [Model card](../../MODEL_CARD.md)
