# Function 4 · When prediction accuracy became the wrong objective

[← All functions](../README.md) · [Project home](../../README.md) · [Observed inputs and outputs](observations.csv) · [Complete decision ledger](selection_history.csv)

**4 inputs · 30 starting observations · 13 rounds**

| Initial best | Final best | First achieved | Best input |
|---:|---:|:---:|---|
| `-4.025542281908162` | **`0.7468979113807426`** | **Round 13** | `0.416903-0.415704-0.360320-0.415205` |

## Understanding this function

F4 improved markedly in the early rounds, then spent several weeks near a best of 0.659. Micro-steps were predicted astonishingly accurately yet gained almost nothing. Widening the local region in R11 returned 0.730459; a further R13 move returned 0.746898. No complete hidden-function equation has been validated.

### Score progression from real evaluations

![Function 4 measured best-so-far history](progress.svg)

The chart tracks measured best-so-far results. A flat interval means no improvement to the incumbent, not that a model predicted a constant function.

## Weekly development · expand a round

Each round shows **what was known or being tested, what was submitted, what returned, and what was learnt**. The original 52-page weekly reflection is the narrative foundation; the decision ledger, surviving code and official portal records establish what was actually submitted. An exact historic kernel/seed/forecast appears only if retained. Where early rationale was reconstructed later, it is explicitly labelled in the ledger.

<details>
<summary><strong>Round 1 · Opening hypothesis</strong> — -1.91054424 ★ new best</summary>

**Original learning context:** Week 1 identified possible multiple good regions and selected a nearby but not identical configuration to test the neighbourhood of an existing observation.

**Strategy / candidate-selection evidence:** GP and acquisition baseline (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.5315-0.448817-0.362651-0.331977`  
**Actual portal result:** `-1.910544236949021`  
**Best observed before → after:** `-4.025542281908162` → `-1.910544236949021`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. Second round: GP/UCB with per-function exploration weights; deterministic candidate grids or pools.

**Supporting material:** [Round 1 evidence](../../journey/round_01/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 2 · GP and UCB working package</strong> — 0.647554265 ★ new best</summary>

**Original learning context:** The first query lifted the best from -4.0255 to -1.9105, so the Week 2 reflection reduced exploration to UCB κ=1.0 to refine the promising region.

**Strategy / candidate-selection evidence:** GP and UCB working package *(early-round attribution partly retrospective)*.

**Submitted input:** `0.415636-0.429159-0.368928-0.413098`  
**Actual portal result:** `0.6475542651940924`  
**Best observed before → after:** `-1.910544236949021` → `0.6475542651940924`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The Week 3 methodology used local EI, exploiting the newly productive area.

**Supporting material:** [Round 2 evidence](../../journey/round_02/README.md) · [Related surviving script/notebook](../../journey/round_02/week2_ucb_course_aligned.py) (related historical script not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 3 · Function-specific EI or wider search (retrospective)</strong> — 0.314899862</summary>

**Original learning context:** The Week 3 methodology used local EI, exploiting the newly productive area.

**Strategy / candidate-selection evidence:** Function-specific EI or wider search (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.398136-0.414095-0.370552-0.440336`  
**Actual portal result:** `0.3148998621282755`  
**Best observed before → after:** `0.6475542651940924` → `0.6475542651940924`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. The original model-comparison reflection highlighted how a small move could change F4 from about 0.648 to 0.315: near-good points were not automatically good.

**Supporting material:** [Round 3 evidence](../../journey/round_03/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 4 · GP, SVM and neural-network diagnostics</strong> — 0.646639136</summary>

**Original learning context:** The original model-comparison reflection highlighted how a small move could change F4 from about 0.648 to 0.315: near-good points were not automatically good.

**Strategy / candidate-selection evidence:** GP, SVM and neural-network diagnostics *(early-round attribution partly retrospective)*.

**Submitted input:** `0.425128-0.426376-0.368659-0.411895`  
**Actual portal result:** `0.646639136105915`  
**Best observed before → after:** `0.6475542651940924` → `0.6475542651940924`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. Controlled probes had raised the observed best to about 0.658927; precision started to dominate the strategy.

**Supporting material:** [Round 4 evidence](../../journey/round_04/README.md) · [Related surviving script/notebook](../../journey/round_04/capstone_bbo_week4_module15.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 5 · Controlled coordinate probes (retrospective)</strong> — 0.658926959 ★ new best</summary>

**Original learning context:** Controlled probes had raised the observed best to about 0.658927; precision started to dominate the strategy.

**Strategy / candidate-selection evidence:** Controlled coordinate probes (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.420382-0.427768-0.368794-0.412497`  
**Actual portal result:** `0.6589269585907762`  
**Best observed before → after:** `0.6475542651940924` → `0.6589269585907762`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. Sixth round: compare GP and MLP using five-fold cross-validated error; treat extra model flexibility as something to justify.

**Supporting material:** [Round 5 evidence](../../journey/round_05/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 6 · GP, ridge and MLP comparison; controlled local fit</strong> — 0.658922504</summary>

**Original learning context:** Sixth round: compare GP and MLP using five-fold cross-validated error; treat extra model flexibility as something to justify.

**Strategy / candidate-selection evidence:** GP, ridge and MLP comparison; controlled local fit *(early-round attribution partly retrospective)*.

**Submitted input:** `0.42029-0.427795-0.368797-0.412509`  
**Actual portal result:** `0.6589225038891553`  
**Best observed before → after:** `0.6589269585907762` → `0.6589269585907762`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. The Week 7 reflection acknowledged diminishing returns: 0.658923 was effectively identical to the previous best of 0.658927.

**Supporting material:** [Round 6 evidence](../../journey/round_06/README.md) · [Related surviving script/notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) (related notebook original fitter missing, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 7 · ARD and local forecast investigations (retrospective)</strong> — 0.658924003</summary>

**Original learning context:** The Week 7 reflection acknowledged diminishing returns: 0.658923 was effectively identical to the previous best of 0.658927.

**Strategy / candidate-selection evidence:** ARD and local forecast investigations (retrospective) *(early-round attribution partly retrospective)*.

**Submitted input:** `0.420383-0.427768-0.368794-0.412497`  
**Actual portal result:** `0.6589240028704428`  
**Best observed before → after:** `0.6589269585907762` → `0.6589269585907762`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. The R8 experiment changed x1 by one millionth while holding three other inputs fixed, testing a local directional hypothesis.

**Supporting material:** [Round 7 evidence](../../journey/round_07/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 8 · Week 7 tested x1 one micro-step to the right of the incumbent and was slight…</strong> — 0.658929913 ★ new best</summary>

**Original learning context:** The R8 experiment changed x1 by one millionth while holding three other inputs fixed, testing a local directional hypothesis.

**Strategy / candidate-selection evidence:** Week 7 tested x1 one micro-step to the right of the incumbent and was slightly worse. Test one micro-step to the left while holding the other coordinates fixed..

**Submitted input:** `0.420381-0.427768-0.368794-0.412497`  
**Actual portal result:** `0.6589299133743123`  
**Best observed before → after:** `0.6589269585907762` → `0.6589299133743123`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The R9 pre-result extrapolation was exceptionally accurate, yet the improvement was minuscule.

**Supporting material:** [Round 8 evidence](../../journey/round_08/README.md) · [Related surviving script/notebook](../../journey/round_08/capstone_bbo_module19_round8.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 9 · Continue the controlled x1 micro-step. The last three comparable observation…</strong> — 0.658932867 ★ new best</summary>

**Original learning context:** The R9 pre-result extrapolation was exceptionally accurate, yet the improvement was minuscule.

**Strategy / candidate-selection evidence:** Continue the controlled x1 micro-step. The last three comparable observations are almost perfectly linear; the extrapolated forecast at x1=0.420380 is about 0.65893287..

**Submitted input:** `0.42038-0.427768-0.368794-0.412497`  
**Actual portal result:** `0.6589328672210581`  
**Best observed before → after:** `0.6589299133743123` → `0.6589328672210581`.

**Pre-result numerical forecast:** `0.6589328687823797` (recorded before return).

**After the result:** The submitted point established a new personal best. The original Week 10 submission gave unusual weight to the precise local forecast, although this reinforced a stalled search region.

**Supporting material:** [Round 9 evidence](../../journey/round_09/README.md) · [Related surviving script/notebook](../../journey/round_09/round9_controlled_fits.py) (related historical analysis not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 10 · Controlled local refinement supported by prospective accuracy</strong> — 0.658962354 ★ new best</summary>

**Original learning context:** The original Week 10 submission gave unusual weight to the precise local forecast, although this reinforced a stalled search region.

**Strategy / candidate-selection evidence:** Controlled local refinement supported by prospective accuracy.

**Submitted input:** `0.420370-0.427768-0.368794-0.412497`  
**Actual portal result:** `0.6589623541690739`  
**Best observed before → after:** `0.6589328672210581` → `0.6589623541690739`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The Week 11 reflection explicitly changed several coordinates together rather than another one-millionth step; the returned best was 0.730459.

**Supporting material:** [Round 10 evidence](../../journey/round_10/README.md) · [Related surviving script/notebook](../../src/bbo/optimizer.py) (related challenger not verified exact, not necessarily the exact historical candidate generator) · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 11 · Alternative-region exploration and structural investigations</strong> — 0.730459421 ★ new best</summary>

**Original learning context:** The Week 11 reflection explicitly changed several coordinates together rather than another one-millionth step; the returned best was 0.730459.

**Strategy / candidate-selection evidence:** Alternative-region exploration and structural investigations.

**Submitted input:** `0.415000-0.417000-0.366500-0.413000`  
**Actual portal result:** `0.7304594213260924`  
**Best observed before → after:** `0.6589623541690739` → `0.7304594213260924`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The Week 12 repeat reproduced the R11 score and supplied no extra nearby observations.

**Supporting material:** [Round 11 evidence](../../journey/round_11/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 12 · Controlled probes, repeats and structural investigations</strong> — 0.730459421</summary>

**Original learning context:** The Week 12 repeat reproduced the R11 score and supplied no extra nearby observations.

**Strategy / candidate-selection evidence:** Controlled probes, repeats and structural investigations.

**Submitted input:** `0.415000-0.417000-0.366500-0.413000`  
**Actual portal result:** `0.7304594213260924`  
**Best observed before → after:** `0.7304594213260924` → `0.7304594213260924`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point did not beat the incumbent. With a finite horizon, the final non-identical local configuration produced the new best, 0.746898.

**Supporting material:** [Round 12 evidence](../../journey/round_12/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

<details>
<summary><strong>Round 13 · Final decision</strong> — 0.746897911 ★ new best</summary>

**Original learning context:** With a finite horizon, the final non-identical local configuration produced the new best, 0.746898.

**Strategy / candidate-selection evidence:** Final exploitation and regional probes.

**Submitted input:** `0.416903-0.415704-0.360320-0.415205`  
**Actual portal result:** `0.7468979113807426`  
**Best observed before → after:** `0.7304594213260924` → `0.7468979113807426`.

**Pre-result numerical forecast:** Not retained as a numerical forecast in the original decision ledger; no value has been invented.

**After the result:** The submitted point established a new personal best. The next query must be worthwhile, not merely predictable. Adjust search width when local precision stops producing material progress.

**Supporting material:** [Round 13 evidence](../../journey/round_13/README.md) · No exact original candidate-selection script retained · [Numerical provenance](selection_history.csv).

</details>

## Visual analysis

<table><tr><td width="50%"><img src="../../results/figures/f4_2d.svg" width="460" alt="Function 4 two-dimensional representation"></td><td width="50%"><img src="../../results/figures/f4_3d.svg" width="460" alt="Function 4 three-dimensional representation"></td></tr></table>

**Observed points only.** These 2D/3D views project the real inputs and their returned scores; no smooth objective surface has been invented. Only x1 and x2 appear on the horizontal axes; x3–x4 vary across observations and the plots do not control for them.

[How the visualisations were produced](../../docs/functions.md) · [Graph-generation code](../../results/figures/build_visual_gallery.mjs)

## Mathematical evidence and its limits

**No validated hidden-function equation is available.** RBF and Matérn GPs, local fits and neural-network challengers are approximate predictive tools, not claims to know the underlying source. The observed maximum in the table is **a personal best**, not a proved global optimum.

## Lessons to carry forward

The next query must be worthwhile, not merely predictable. Adjust search width when local precision stops producing material progress.

**Source discipline:** The originally submitted weekly reflections informed the learning context; the portal results and preserved files establish what actually happened. Historical experiments, post-outcome explanations and model-generated graph values are not interchangeable.

[← All eight functions](../README.md) · [Dataset description](../../DATASHEET.md) · [Model card](../../MODEL_CARD.md)
