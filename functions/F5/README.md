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

Each round shows **what was known or being tested, what was submitted, what returned, and what was learnt**. The original 52-page weekly reflection is the narrative foundation; the decision ledger, surviving code and official portal records establish what was actually submitted. An exact historic kernel/seed/forecast appears only if retained. Where early rationale was reconstructed later, it is explicitly labelled in the ledger.

<details>
<summary><strong>Round 1 · Opening hypothesis</strong> — 1426.08976 ★ new best</summary>

**Original learning context:** The original first reflection expected one main chemical-yield peak and chose a stronger area for exploitation rather than global search.

**Strategy / candidate-selection evidence:** GP and acquisition baseline (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.1-0.75-0.9-0.98`  
**Actual portal result:** `1426.0897645116545`  
**Best observed before → after:** `1088.8596181962705` → `1426.0897645116545`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. Second round: GP/UCB with per-function exploration weights; deterministic candidate grids or pools.

**Supporting material:** [Round 1 evidence](../../journey/round_01/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 2 · GP and UCB working package</strong> — 3722.27447 ★ new best</summary>

**Original learning context:** After R1 improved to 1426.09, Week 2 gave F5 the exploitative UCB κ=1.0 and noted that later coordinates near their upper bounds were important.

**Strategy / candidate-selection evidence:** GP and UCB working package *(early-round attribution partly retrospective)*.

**Submitted input:** `0.522156-0.922246-0.999259-0.99589`  
**Actual portal result:** `3722.27447382346`  
**Best observed before → after:** `1426.0897645116545` → `3722.27447382346`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The Week 3 strategy used local Expected Improvement because the prior queries kept increasing the best.

**Supporting material:** [Round 2 evidence](../../journey/round_02/README.md) · [Related surviving script/notebook](../../journey/round_02/week2_ucb_course_aligned.py) (related historical script not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 3 · Function-specific EI or wider search (retrospective)</strong> — 4295.86773 ★ new best</summary>

**Original learning context:** The Week 3 strategy used local Expected Improvement because the prior queries kept increasing the best.

**Strategy / candidate-selection evidence:** Function-specific EI or wider search (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.508373-0.970147-0.999999-0.999999`  
**Actual portal result:** `4295.86773060836`  
**Best observed before → after:** `3722.27447382346` → `4295.86773060836`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The Week 5 original reflection documents the R4 single-coordinate test: x2 moved from 0.970147 to 0.999999, raising 4295.87 to 4694.32.

**Supporting material:** [Round 3 evidence](../../journey/round_03/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 4 · GP, SVM and neural-network diagnostics</strong> — 4694.31731 ★ new best</summary>

**Original learning context:** The Week 5 original reflection documents the R4 single-coordinate test: x2 moved from 0.970147 to 0.999999, raising 4295.87 to 4694.32.

**Strategy / candidate-selection evidence:** GP, SVM and neural-network diagnostics *(early-round attribution partly retrospective)*.

**Submitted input:** `0.508373-0.999999-0.999999-0.999999`  
**Actual portal result:** `4694.317308235808`  
**Best observed before → after:** `4295.86773060836` → `4694.317308235808`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The next controlled x1 increase, holding x2–x4 fixed, improved the score again.

**Supporting material:** [Round 4 evidence](../../journey/round_04/README.md) · [Related surviving script/notebook](../../journey/round_04/capstone_bbo_week4_module15.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 5 · Controlled coordinate probes (retrospective)</strong> — 4807.98608 ★ new best</summary>

**Original learning context:** The next controlled x1 increase, holding x2–x4 fixed, improved the score again.

**Strategy / candidate-selection evidence:** Controlled coordinate probes (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.558373-0.999999-0.999999-0.999999`  
**Actual portal result:** `4807.986076589498`  
**Best observed before → after:** `4694.317308235808` → `4807.986076589498`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. Original Week 6 work describes the contrast between a large early breakthrough and incremental local improvement on F5.

**Supporting material:** [Round 5 evidence](../../journey/round_05/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 6 · GP, ridge and MLP comparison; controlled local fit</strong> — 4957.57171 ★ new best</summary>

**Original learning context:** Original Week 6 work describes the contrast between a large early breakthrough and incremental local improvement on F5.

**Strategy / candidate-selection evidence:** GP, ridge and MLP comparison; controlled local fit *(early-round attribution partly retrospective)*.

**Submitted input:** `0.608373-0.999999-0.999999-0.999999`  
**Actual portal result:** `4957.571711515816`  
**Best observed before → after:** `4807.986076589498` → `4957.571711515816`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Supporting material:** [Round 6 evidence](../../journey/round_06/README.md) · [Related surviving script/notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) (related notebook original fitter missing, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 7 · ARD and local forecast investigations (retrospective)</strong> — 5151.04773 ★ new best</summary>

**Original learning context:** Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Strategy / candidate-selection evidence:** ARD and local forecast investigations (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.658373-0.999999-0.999999-0.999999`  
**Actual portal result:** `5151.047725485012`  
**Best observed before → after:** `4957.571711515816` → `5151.047725485012`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The Week 8/9 reflections showed gains accelerating along the same x1 path; smaller steps were not automatically safer or better.

**Supporting material:** [Round 7 evidence](../../journey/round_07/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 8 · The controlled x1 series remains monotonic with accelerating gains. Increase…</strong> — 5709.36132 ★ new best</summary>

**Original learning context:** The Week 8/9 reflections showed gains accelerating along the same x1 path; smaller steps were not automatically safer or better.

**Strategy / candidate-selection evidence:** The controlled x1 series remains monotonic with accelerating gains. Increase x1 by 0.10 while retaining x2-x4 at the validated upper boundary..

**Submitted input:** `0.758373-0.999999-0.999999-0.999999`  
**Actual portal result:** `5709.3613198927205`  
**Best observed before → after:** `5151.047725485012` → `5709.3613198927205`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. Week 9 emphasised that the prior F5 gain of 558.31 justified another larger step, rather than a default diminishing-returns assumption.

**Supporting material:** [Round 8 evidence](../../journey/round_08/README.md) · [Related surviving script/notebook](../../journey/round_08/capstone_bbo_module19_round8.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 9 · Continue the validated boundary trajectory with a 0.10 x1 step. Marginal gai…</strong> — 6583.56145 ★ new best</summary>

**Original learning context:** Week 9 emphasised that the prior F5 gain of 558.31 justified another larger step, rather than a default diminishing-returns assumption.

**Strategy / candidate-selection evidence:** Continue the validated boundary trajectory with a 0.10 x1 step. Marginal gain per unit x1 has been increasing, and independent local quadratic / GP checks both forecast roughly 6454..

**Submitted input:** `0.858373-0.999999-0.999999-0.999999`  
**Actual portal result:** `6583.56144525802`  
**Best observed before → after:** `5709.3613198927205` → `6583.56144525802`.

**Pre-result numerical forecast:** `6454.0` (recorded before return).

**After the result:** The submitted point established a new personal best. The original Round 10 decision says that nine successive gains justified testing every coordinate at the legal upper corner, with external cubic/challenger support.

**Supporting material:** [Round 9 evidence](../../journey/round_09/README.md) · [Related surviving script/notebook](../../journey/round_09/round9_controlled_fits.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 10 · Upper-bound exploitation supported by nine observed gains and cubic challenger</strong> — 8662.40500 ★ new best</summary>

**Original learning context:** The original Round 10 decision says that nine successive gains justified testing every coordinate at the legal upper corner, with external cubic/challenger support.

**Strategy / candidate-selection evidence:** Upper-bound exploitation supported by nine observed gains and cubic challenger.

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Actual portal result:** `8662.405001248297`  
**Best observed before → after:** `6583.56144525802` → `8662.405001248297`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. Repeating the confirmed boundary score did not establish a hidden-source global optimum.

**Supporting material:** [Round 10 evidence](../../journey/round_10/README.md) · [Related surviving script/notebook](../../src/bbo/optimizer.py) (related challenger not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 11 · Alternative-region exploration and structural investigations</strong> — 8662.40500</summary>

**Original learning context:** Repeating the confirmed boundary score did not establish a hidden-source global optimum.

**Strategy / candidate-selection evidence:** Alternative-region exploration and structural investigations.

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Actual portal result:** `8662.405001248297`  
**Best observed before → after:** `8662.405001248297` → `8662.405001248297`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Another repeat held the incumbent while teaching little about other inputs.

**Supporting material:** [Round 11 evidence](../../journey/round_11/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 12 · Controlled probes, repeats and structural investigations</strong> — 8662.40500</summary>

**Original learning context:** Another repeat held the incumbent while teaching little about other inputs.

**Strategy / candidate-selection evidence:** Controlled probes, repeats and structural investigations.

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Actual portal result:** `8662.405001248297`  
**Best observed before → after:** `8662.405001248297` → `8662.405001248297`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. The final record again retained the highest legal tested point; the mathematically reconstructed power-sum function came from later analysis.

**Supporting material:** [Round 12 evidence](../../journey/round_12/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 13 · Final decision</strong> — 8662.40500</summary>

**Original learning context:** The final record again retained the highest legal tested point; the mathematically reconstructed power-sum function came from later analysis.

**Strategy / candidate-selection evidence:** Final exploitation and regional probes.

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Actual portal result:** `8662.405001248297`  
**Best observed before → after:** `8662.405001248297` → `8662.405001248297`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Boundary tests are justified when they answer a concrete, evidence-supported question. Avoid claiming that a retrospective equation drove an earlier query.

**Supporting material:** [Round 13 evidence](../../journey/round_13/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

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

At the legal upper input of **(0.999999)⁴**, the equation returns **8662.405001248297**, matching the portal. At the unpermitted (1,1,1,1), it predicts 8662.4825. **This equation was recovered after R10 and did not select the original boundary query.** It is corroborated on tested inputs, not proven to be the undisclosed implementation globally.

## Lessons to carry forward

Boundary tests are justified when they answer a concrete, evidence-supported question. Avoid claiming that a retrospective equation drove an earlier query.

**Source discipline:** The originally submitted weekly reflections informed the learning context; the portal results and preserved files establish what actually happened. Historical experiments, post-outcome explanations and model-generated graph values are not interchangeable.

[← All eight functions](../README.md) · [Dataset description](../../DATASHEET.md) · [Model card](../../MODEL_CARD.md)
