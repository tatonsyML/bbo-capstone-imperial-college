# Function 5 · Controlled steps to a productive boundary

[← All functions](../README.md) · [Project home](../../README.md) · [Observed inputs and outputs](observations.csv) · [Complete decision ledger](selection_history.csv)

**4 inputs · 20 starting observations · 13 rounds**

| Initial best | Final best | First achieved | Best input |
|---:|---:|:---:|---|
| `1088.8596181962705` | **`8662.405001248297`** | **Round 10** | `0.999999-0.999999-0.999999-0.999999` |

## Understanding this function

F5 had a strong directional signal. A sequence of controlled coordinate changes showed increasing scores towards the legal upper boundary; R10 tested (0.999999)⁴ and returned 8662.405. The full interacting power-sum equation was reconstructed **after** the boundary query, so it explains rather than caused that decision.

### Score progression from real evaluations

![Function 5 measured best-so-far history](progress.svg)

The chart tracks measured best-so-far results. A flat interval means no improvement to the incumbent, not that a model predicted a constant function.

## Weekly development · expand a round

<details>
<summary><strong>Round 1 · Opening hypothesis</strong> — 1426.08976 ★ new best</summary>

**Reasoning:** The original first reflection expected one main chemical-yield peak and chose a stronger area for exploitation rather than global search.

**Approach:** GP and acquisition baseline.

**Submitted input:** `0.1-0.75-0.9-0.98`  
**Result:** `1426.0897645116545`  
**Best observed before → after:** `1088.8596181962705` → `1426.0897645116545`.

**What I learnt:** The submitted point established a new personal best. Second round: GP/UCB with per-function exploration weights; deterministic candidate grids or pools.

**Code and results:** [Round 1 research](../../journey/round_01/README.md) · [Submitted inputs](../../journey/round_01/queries.txt) · [Returned scores](../../journey/round_01/outputs.txt) · [Original coursework notebook](../../journey/round_01/supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb) (coursework, not a verified portal generator) · No separate candidate-generator source authenticated · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 2 · GP and UCB working package</strong> — 3722.27447 ★ new best</summary>

**Reasoning:** After R1 improved to 1426.09, Week 2 gave F5 the exploitative UCB κ=1.0 and noted that later coordinates near their upper bounds were important.

**Approach:** GP and UCB working package.

**Submitted input:** `0.522156-0.922246-0.999259-0.99589`  
**Result:** `3722.27447382346`  
**Best observed before → after:** `1426.0897645116545` → `3722.27447382346`.

**What I learnt:** The submitted point established a new personal best. The Week 3 strategy used local Expected Improvement because the prior queries kept increasing the best.

**Code and results:** [Round 2 research](../../journey/round_02/README.md) · [Submitted inputs](../../journey/round_02/queries.txt) · [Returned scores](../../journey/round_02/outputs.txt) · [Original GP/UCB selection script](../../journey/round_02/week2_ucb_course_aligned.py) · [Eight saved selections](../../journey/round_02/week2_ucb_results.csv) (all eight saved portal values match the submitted record) · [Notebook](../../journey/round_02/Capstone_BBO_Week2_UCB_only.ipynb) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 3 · Function-specific EI or wider search</strong> — 4295.86773 ★ new best</summary>

**Reasoning:** The Week 3 strategy used local Expected Improvement because the prior queries kept increasing the best.

**Approach:** Function-specific EI or wider search.

**Submitted input:** `0.508373-0.970147-0.999999-0.999999`  
**Result:** `4295.86773060836`  
**Best observed before → after:** `3722.27447382346` → `4295.86773060836`.

**What I learnt:** The submitted point established a new personal best. The Week 5 original reflection documents the R4 single-coordinate test: x2 moved from 0.970147 to 0.999999, raising 4295.87 to 4694.32.

**Code and results:** [Round 3 research](../../journey/round_03/README.md) · [Submitted inputs](../../journey/round_03/queries.txt) · [Returned scores](../../journey/round_03/outputs.txt) · The original reflection records function-specific acquisition choices; no standalone original query generator is preserved for this round · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 4 · GP, SVM and neural-network diagnostics</strong> — 4694.31731 ★ new best</summary>

**Reasoning:** The Week 5 original reflection documents the R4 single-coordinate test: x2 moved from 0.970147 to 0.999999, raising 4295.87 to 4694.32.

**Approach:** GP, SVM and neural-network diagnostics.

**Submitted input:** `0.508373-0.999999-0.999999-0.999999`  
**Result:** `4694.317308235808`  
**Best observed before → after:** `4295.86773060836` → `4694.317308235808`.

**What I learnt:** The submitted point established a new personal best. The next controlled x1 increase, holding x2–x4 fixed, improved the score again.

**Code and results:** [Round 4 research](../../journey/round_04/README.md) · [Submitted inputs](../../journey/round_04/queries.txt) · [Returned scores](../../journey/round_04/outputs.txt) · [Original analysis code](../../journey/round_04/capstone_bbo_week4_module15.py) · [Executed notebook](../../journey/round_04/Capstone_BBO_Week4_Module15.ipynb) (final eight inputs stored explicitly; hybrid selection, not an autonomous selector) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 5 · Controlled coordinate probes</strong> — 4807.98608 ★ new best</summary>

**Reasoning:** The next controlled x1 increase, holding x2–x4 fixed, improved the score again.

**Approach:** Controlled coordinate probes.

**Submitted input:** `0.558373-0.999999-0.999999-0.999999`  
**Result:** `4807.986076589498`  
**Best observed before → after:** `4694.317308235808` → `4807.986076589498`.

**What I learnt:** The submitted point established a new personal best. Original Week 6 work describes the contrast between a large early breakthrough and incremental local improvement on F5.

**Code and results:** [Round 5 research](../../journey/round_05/README.md) · [Submitted inputs](../../journey/round_05/queries.txt) · [Returned scores](../../journey/round_05/outputs.txt) · Contemporary reflection and submitted measurements preserved; no standalone selection code authenticated · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 6 · GP, ridge and MLP comparison; controlled local fit</strong> — 4957.57171 ★ new best</summary>

**Reasoning:** Original Week 6 work describes the contrast between a large early breakthrough and incremental local improvement on F5.

**Approach:** GP, ridge and MLP comparison; controlled local fit.

**Submitted input:** `0.608373-0.999999-0.999999-0.999999`  
**Result:** `4957.571711515816`  
**Best observed before → after:** `4807.986076589498` → `4957.571711515816`.

**What I learnt:** The submitted point established a new personal best. Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Code and results:** [Round 6 research](../../journey/round_06/README.md) · [Submitted inputs](../../journey/round_06/queries.txt) · [Returned scores](../../journey/round_06/outputs.txt) · [Original Module 17 notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) · [Eight selected inputs](../../journey/round_06/results/round6_queries.csv) · [Decision rationale](../../journey/round_06/results/round6_query_rationale.csv) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 7 · ARD and local forecast investigations</strong> — 5151.04773 ★ new best</summary>

**Reasoning:** Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Approach:** ARD and local forecast investigations.

**Submitted input:** `0.658373-0.999999-0.999999-0.999999`  
**Result:** `5151.047725485012`  
**Best observed before → after:** `4957.571711515816` → `5151.047725485012`.

**What I learnt:** The submitted point established a new personal best. The Week 8/9 reflections showed gains accelerating along the same x1 path; smaller steps were not automatically safer or better.

**Code and results:** [Round 7 research](../../journey/round_07/README.md) · [Submitted inputs](../../journey/round_07/queries.txt) · [Returned scores](../../journey/round_07/outputs.txt) · [Week 7 forecast comparisons](../../journey/round_08/results/week7_audit.csv) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 8 · Extending the improving x1 trajectory</strong> — 5709.36132 ★ new best</summary>

**Reasoning:** The Week 8/9 reflections showed gains accelerating along the same x1 path; smaller steps were not automatically safer or better.

**Approach:** The controlled x1 series remains monotonic with accelerating gains. Increase x1 by 0.10 while retaining x2-x4 at the validated upper boundary..

**Submitted input:** `0.758373-0.999999-0.999999-0.999999`  
**Result:** `5709.3613198927205`  
**Best observed before → after:** `5151.047725485012` → `5709.3613198927205`.

**Forecast preserved before the Round 8 return:** approximately `5654.123` (local quadratic; see [Round 8 forecast table](../../journey/round_08/README.md)).

**What I learnt:** The submitted point established a new personal best. Week 9 emphasised that the prior F5 gain of 558.31 justified another larger step, rather than a default diminishing-returns assumption.

**Code and results:** [Round 8 research](../../journey/round_08/README.md) · [Submitted inputs](../../journey/round_08/queries.txt) · [Returned scores](../../journey/round_08/outputs.txt) · [Original Module 19 Python analysis](../../journey/round_08/capstone_bbo_module19_round8.py) · [Original eight-input decision record](../../journey/round_08/results/round8_queries.csv) (all eight match portal inputs) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 9 · Another step towards the upper boundary</strong> — 6583.56145 ★ new best</summary>

**Reasoning:** Week 9 emphasised that the prior F5 gain of 558.31 justified another larger step, rather than a default diminishing-returns assumption.

**Approach:** Continue the validated boundary trajectory with a 0.10 x1 step. Marginal gain per unit x1 has been increasing, and independent local quadratic / GP checks both forecast roughly 6454..

**Submitted input:** `0.858373-0.999999-0.999999-0.999999`  
**Result:** `6583.56144525802`  
**Best observed before → after:** `5709.3613198927205` → `6583.56144525802`.

**Pre-result numerical forecast:** `6454.0` (recorded before return).

**What I learnt:** The submitted point established a new personal best. The original Round 10 decision says that nine successive gains justified testing every coordinate at the legal upper corner, with external cubic/challenger support.

**Code and results:** [Round 9 research](../../journey/round_09/README.md) · [Submitted inputs](../../journey/round_09/queries.txt) · [Returned scores](../../journey/round_09/outputs.txt) · [Dated eight-input decision and forecast ledger](../../journey/round_09/results/round9_queries.csv) (all eight match portal inputs) · [Original controlled local-fitting code](../../journey/round_09/round9_controlled_fits.py) (includes F5 analysis) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 10 · Upper-bound exploitation supported by nine observed gains and cubic challenger</strong> — 8662.40500 ★ new best</summary>

**Reasoning:** The original Round 10 decision says that nine successive gains justified testing every coordinate at the legal upper corner, with external cubic/challenger support.

**Approach:** Upper-bound exploitation supported by nine observed gains and cubic challenger.

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Result:** `8662.405001248297`  
**Best observed before → after:** `6583.56144525802` → `8662.405001248297`.

**What I learnt:** The submitted point established a new personal best. Repeating the confirmed boundary score did not establish a hidden-source global optimum.

**Code and results:** [Round 10 research](../../journey/round_10/README.md) · [Submitted inputs](../../journey/round_10/queries.txt) · [Returned scores](../../journey/round_10/outputs.txt) · [Dated final candidate list](../../journey/round_10/round10_candidates.csv) · [Pre-result planning snapshot](../../journey/round_10/optimisation.yaml) · [GP/HEBO-inspired/TuRBO-style challenger code](../../src/bbo/optimizer.py) (not proof of the exact final per-function generator) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 11 · Alternative-region exploration and structural investigations</strong> — 8662.40500</summary>

**Reasoning:** Repeating the confirmed boundary score did not establish a hidden-source global optimum.

**Approach:** Alternative-region exploration and structural investigations.

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Result:** `8662.405001248297`  
**Best observed before → after:** `8662.405001248297` → `8662.405001248297`.

**What I learnt:** The submitted point did not beat the incumbent. Another repeat held the incumbent while teaching little about other inputs.

**Code and results:** [Round 11 research](../../journey/round_11/README.md) · [Portal inputs/outputs for R11](../../data/portal_rounds_11_12.csv) · [Later reproducible DBSCAN diagnostic](../../research/diagnostics/clustering/clustering_audit.py) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 12 · Controlled probes, repeats and structural investigations</strong> — 8662.40500</summary>

**Reasoning:** Another repeat held the incumbent while teaching little about other inputs.

**Approach:** Controlled probes, repeats and structural investigations.

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Result:** `8662.405001248297`  
**Best observed before → after:** `8662.405001248297` → `8662.405001248297`.

**What I learnt:** The submitted point did not beat the incumbent. The final record again retained the highest legal tested point; the mathematically reconstructed power-sum function came from later analysis.

**Supporting material:** [Round 12 evidence](../../journey/round_12/README.md) · [Dated Round 12 recommendations](../../journey/round_12/original/week12_full_review_2026-11-02.md) (records the boundary repeat) · [Decision history](selection_history.csv).

</details>

<details>
<summary><strong>Round 13 · Final decision</strong> — 8662.40500</summary>

**Reasoning:** The final record again retained the highest legal tested point; the mathematically reconstructed power-sum function came from later analysis.

**Approach:** Final exploitation and regional probes.

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Result:** `8662.405001248297`  
**Best observed before → after:** `8662.405001248297` → `8662.405001248297`.

**What I learnt:** The submitted point did not beat the incumbent. Boundary tests are justified when they answer a concrete, evidence-supported question. The equation was fitted later to explain the measured pattern.

**Code and results:** [Round 13 research](../../journey/round_13/README.md) · [Submitted inputs](../../journey/round_13/queries.txt) · [Returned scores](../../journey/round_13/outputs.txt) · [Final thirteen-round reflection](../../journey/final_reflection/README.md) (final reasoning, not a surviving standalone selector) · [Decision history](selection_history.csv).

</details>

## Visual analysis

<table><tr><td width="50%"><img src="../../results/figures/f5_2d.svg" width="460" alt="Function 5 two-dimensional representation"></td><td width="50%"><img src="../../results/figures/f5_3d.svg" width="460" alt="Function 5 three-dimensional representation"></td></tr></table>

**Model slices, not additional observations:** the two charts vary x1 and x2, holding **x3=x4=0.999999**. The graph shows **log1p(output)** to make the steep response readable. The real measured points are in the ledger above.

[How the visualisations were produced](../../docs/functions.md) · [Graph-generation code](../../results/figures/build_visual_gallery.mjs)

## Mathematical evidence and its limits

A retrospective reconstruction of F5 is the interacting power-sum expression:

$$
\hat f_5(\mathbf{x}) = 0.01\sum_{k=1}^{4}\left[\sum_{j=1}^{4}(4x_j)^k-b_k\right]^2,\quad\mathbf{b}=(7.5,16,40,120).
$$

At the legal upper input of **(0.999999)⁴**, the equation returns **8662.405001248297**, matching the portal. At the unpermitted (1,1,1,1), it predicts 8662.4825. **This equation was reconstructed after R10 and did not select the original boundary query.** It is corroborated on tested inputs, not proven to be the undisclosed implementation globally.

## Lessons to carry forward

Boundary tests are justified when they answer a concrete, evidence-supported question. The equation was fitted later to explain the measured pattern.

**Source discipline:** The originally submitted weekly reflections informed the learning context; the portal results and preserved files establish what actually happened. Historical experiments, post-outcome explanations and model-generated graph values are not interchangeable.

[← All eight functions](../README.md) · [Dataset description](../../DATASHEET.md) · [Model card](../../MODEL_CARD.md)
