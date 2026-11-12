# Function 3 · Learning when a fitted local peak is misleading

**Function navigation (3/8):** [← Previous: F2](../F2/README.md) · [All eight functions](../README.md) · [Next: F4 →](../F4/README.md)
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

**Why this input:** The original first reflection noted that the best outputs were already close to zero and favoured cautious exploitation while retaining a promising coordinate.

**Approach considered:** Cautious exploitation near strong negative scores (higher is nearer zero), while treating GP/EI as exploratory decision ideas, not a confirmed automated Round 1 generator.

**Submitted input:** `0.5-0.5-0.345`  
**Actual portal result:** `-0.0437772384849064`  
**Best observed before → after:** `-0.034835313350078584` → `-0.034835313350078584`.

**What I learnt:** The first query scored below the initial best; interpolation did not improve the known solution.

**Code and data:** [Round notes](../../journey/round_01/README.md) · [Inputs](../../journey/round_01/queries.txt) · [Outputs](../../journey/round_01/outputs.txt) · [Coursework notebook](../../journey/round_01/supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb).

</details>

<details>
<summary><strong>Round 2 · GP and UCB working package</strong> — -0.106495098</summary>

**Why this input:** The first return was close to, but worse than, the starting best; Week 2 used a balanced UCB setting κ=2.0.

**Approach considered:** GP/UCB with κ=2.0 balanced exploration and exploitation after the first result failed to improve the supplied incumbent.

**Submitted input:** `0.993188-0.591985-0.00028`  
**Actual portal result:** `-0.1064950977729621`  
**Best observed before → after:** `-0.034835313350078584` → `-0.034835313350078584`.

**What I learnt:** The broader GP/UCB candidate scored substantially worse, so exploration needed better direction.

**Code and data:** [Round notes](../../journey/round_02/README.md) · [Inputs](../../journey/round_02/queries.txt) · [Outputs](../../journey/round_02/outputs.txt) · [GP/UCB Python code](../../journey/round_02/week2_ucb_course_aligned.py) · [Saved candidates](../../journey/round_02/week2_ucb_results.csv) · [Notebook](../../journey/round_02/Capstone_BBO_Week2_UCB_only.ipynb).

</details>

<details>
<summary><strong>Round 3 · Function-specific EI or wider search</strong> — -0.0427365724</summary>

**Why this input:** The Week 3 plan explicitly selected local predicted-mean optimisation for F3, not the globally exploratory EI used for F2.

**Approach considered:** Local predicted-mean optimisation, not a blanket EI rule, refined a promising observed region using normalised GP targets.

**Submitted input:** `0.496377-0.564413-0.34369`  
**Actual portal result:** `-0.0427365723752823`  
**Best observed before → after:** `-0.034835313350078584` → `-0.034835313350078584`.

**What I learnt:** The result improved on the preceding query but did not exceed the initial incumbent.

**Code and data:** [Round notes](../../journey/round_03/README.md) · [Inputs](../../journey/round_03/queries.txt) · [Outputs](../../journey/round_03/outputs.txt).

</details>

<details>
<summary><strong>Round 4 · GP, SVM and neural-network diagnostics</strong> — -0.0312815968 ★ new best</summary>

**Why this input:** After early GP-led comparisons, I tested a different candidate rather than assuming that the poor initial returns described the whole region.

**Approach considered:** GP remained the primary surrogate, with SVM classification and neural-network gradients as secondary evidence rather than a hard veto on candidates.

**Submitted input:** `0.49-0.62-0.36`  
**Actual portal result:** `-0.0312815968234451`  
**Best observed before → after:** `-0.034835313350078584` → `-0.0312815968234451`.

**What I learnt:** A different candidate improved the best score, showing that the earlier poor returns did not rule out progress.

**Code and data:** [Round notes](../../journey/round_04/README.md) · [Inputs](../../journey/round_04/queries.txt) · [Outputs](../../journey/round_04/outputs.txt) · [Python analysis](../../journey/round_04/capstone_bbo_week4_module15.py) · [Notebook](../../journey/round_04/Capstone_BBO_Week4_Module15.ipynb).

</details>

<details>
<summary><strong>Round 5 · Controlled coordinate probes</strong> — -0.0334231088</summary>

**Why this input:** Fifth round: use controlled coordinate differences to avoid confusing a multi-variable shift with a causal single-input effect.

**Approach considered:** Controlled coordinate probes tested local response and interactions instead of assuming separate input effects.

**Submitted input:** `0.483623-0.675587-0.37631`  
**Actual portal result:** `-0.0334231088352711`  
**Best observed before → after:** `-0.0312815968234451` → `-0.0312815968234451`.

**What I learnt:** The controlled probe scored below the new incumbent, highlighting how fragile nearby improvements were.

**Code and data:** [Round notes](../../journey/round_05/README.md) · [Inputs](../../journey/round_05/queries.txt) · [Outputs](../../journey/round_05/outputs.txt).

</details>

<details>
<summary><strong>Round 6 · GP, ridge and MLP comparison; controlled local fit</strong> — -0.0208561545 ★ new best</summary>

**Why this input:** Original five-fold validation found that a small MLP slightly outperformed the GP on F3, unlike F7/F8. This challenged uncritical model preference.

**Approach considered:** Five-fold GP/MLP comparison and local fitting challenged GP authority where the small MLP's validation error was lower for F3.

**Submitted input:** `0.487816-0.639038-0.365586`  
**Actual portal result:** `-0.0208561545295093`  
**Best observed before → after:** `-0.0312815968234451` → `-0.0208561545295093`.

**What I learnt:** The new input raised the best score and justified continuing carefully selected tests.

**Code and data:** [Round notes](../../journey/round_06/README.md) · [Inputs](../../journey/round_06/queries.txt) · [Outputs](../../journey/round_06/outputs.txt) · [Notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) · [Eight selected inputs](../../journey/round_06/results/round6_queries.csv) · [Decision notes](../../journey/round_06/results/round6_query_rationale.csv).

</details>

<details>
<summary><strong>Round 7 · ARD and local forecast investigations</strong> — -0.0279111486</summary>

**Why this input:** Seventh round: compare RBF and Matérn, ARD, noise and rolling-origin forecast accuracy rather than fitting alone.

**Approach considered:** RBF/Matérn, ARD, noise and rolling-origin checks tested uncertain local extrapolation against later returned scores.

**Submitted input:** `0.486949-0.646592-0.367803`  
**Actual portal result:** `-0.0279111486430777`  
**Best observed before → after:** `-0.0208561545295093` → `-0.0208561545295093`.

**What I learnt:** Another local candidate failed to improve the best, despite model and kernel investigations.

**Code and data:** [Round notes](../../journey/round_07/README.md) · [Inputs](../../journey/round_07/queries.txt) · [Outputs](../../journey/round_07/outputs.txt) · [Forecast comparison](../../journey/round_08/results/week7_audit.csv).

</details>

<details>
<summary><strong>Round 8 · Testing the local quadratic after an overshoot</strong> — -0.0296632774</summary>

**Why this input:** A local quadratic suggested an improved score along the existing path. I submitted the candidate to test that extrapolation.

**Approach considered:** Week 7 overshot the Week 6 local best. A quadratic through the left bracket, Week 6 best and Week 7 point places the local vertex back at t≈0.260 on the controlled path.

**Submitted input:** `0.488344-0.634434-0.364235`  
**Actual portal result:** `-0.0296632773887996`  
**Best observed before → after:** `-0.0208561545295093` → `-0.0208561545295093`.

**Pre-result forecast:** approximately `−0.019675` (local-path model; see [Round 8 forecast table](../../journey/round_08/README.md)).

**What I learnt:** The preserved forecast was too optimistic: the portal returned a materially lower score.

**Code and data:** [Round notes](../../journey/round_08/README.md) · [Inputs](../../journey/round_08/queries.txt) · [Outputs](../../journey/round_08/outputs.txt) · [Python analysis](../../journey/round_08/capstone_bbo_module19_round8.py) · [Saved candidates](../../journey/round_08/results/round8_queries.csv).

</details>

<details>
<summary><strong>Round 9 · Updating the local-path quadratic</strong> — -0.0258164064</summary>

**Why this input:** The original Week 9 reflection warned that an optimistic F3 forecast near -0.01968 had returned around -0.02966.

**Approach considered:** Updated local-path quadratic using Week 8, Week 6 and Week 7 places the vertex near this point, predicting about -0.02011. This is a tighter bracket after two forecast misses.

**Submitted input:** `0.487611-0.640821-0.366109`  
**Actual portal result:** `-0.0258164064206346`  
**Best observed before → after:** `-0.0208561545295093` → `-0.0208561545295093`.

**Pre-result forecast:** `-0.02011192237870145` (recorded before return).

**What I learnt:** The revised local-path forecast missed again, showing that a tighter local fit was not yet reliable.

**Code and data:** [Round notes](../../journey/round_09/README.md) · [Inputs](../../journey/round_09/queries.txt) · [Outputs](../../journey/round_09/outputs.txt) · [Candidate forecasts](../../journey/round_09/results/round9_queries.csv) · [Original controlled local-fitting code](../../journey/round_09/round9_controlled_fits.py).

</details>

<details>
<summary><strong>Round 10 · Alternative-region local interpolation; external evidence; uncertain</strong> — -0.0146028106 ★ new best</summary>

**Why this input:** The Week 10 submission describes rejecting a speculative restart in favour of an alternative x3 region, partly informed by separately attributed external data.

**Approach considered:** Alternative-region local interpolation; external evidence; uncertain.

**Submitted input:** `0.469634-0.620072-0.416672`  
**Actual portal result:** `-0.014602810625106634`  
**Best observed before → after:** `-0.0208561545295093` → `-0.014602810625106634`.

**What I learnt:** A different region improved the best score, challenging the earlier local-search assumptions.

**Code and data:** [Round notes](../../journey/round_10/README.md) · [Inputs](../../journey/round_10/queries.txt) · [Outputs](../../journey/round_10/outputs.txt) · [Candidate list](../../journey/round_10/round10_candidates.csv) · [Search plan](../../journey/round_10/optimisation.yaml) · [Related optimiser code](../../src/bbo/optimizer.py).

</details>

<details>
<summary><strong>Round 11 · Improving in a different region</strong> — -0.00570922028 ★ new best</summary>

**Why this input:** Eleventh round: analyse density with DBSCAN but do not confuse sampled clusters with high-performing regions.

**Approach considered:** Alternative-region exploration and structural investigations.

**Submitted input:** `0.445500-0.593000-0.420000`  
**Actual portal result:** `-0.005709220275560069`  
**Best observed before → after:** `-0.014602810625106634` → `-0.005709220275560069`.

**What I learnt:** Another alternative-region test improved the incumbent to approximately −0.005709.

**Code and data:** [Round notes](../../journey/round_11/README.md) · [Portal results](../../data/portal_rounds_11_12.csv) · [Clustering analysis (later reproduction)](../../research/diagnostics/clustering/clustering_audit.py).

</details>

<details>
<summary><strong>Round 12 · Testing beyond the new incumbent</strong> — -0.0226526646</summary>

**Why this input:** After Round 11 improved the best to approximately −0.005709, I tested a wider alternative to explore beyond the incumbent.

**Approach considered:** Alternative-region probe.

**Submitted input:** `0.313581-0.474345-0.485191`  
**Actual portal result:** `-0.0226526646178297`  
**Best observed before → after:** `-0.005709220275560069` → `-0.005709220275560069`.

**What I learnt:** The wider candidate scored below the Round 11 best; exploring new regions still incurred an opportunity cost.

**Code and data:** [Round notes](../../journey/round_12/README.md) · [Round 12 Python](../../journey/round_12/original/review_round12.py) · [Original TPE and local-model comparisons](../../journey/round_12/original/tpe_local.py) · [Dated candidate rationale](../../journey/round_12/original/week12_full_review_2026-11-02.md).

</details>

<details>
<summary><strong>Round 13 · Final alternative-region test</strong> — -0.00375309692 ★ new best</summary>

**Why this input:** With one query remaining and Round 12 below the incumbent, I tested another candidate in a different region.

**Approach considered:** Final exploration of a competing region.

**Submitted input:** `0.197280-0.523429-0.470094`  
**Actual portal result:** `-0.0037530969187192596`  
**Best observed before → after:** `-0.005709220275560069` → `-0.0037530969187192596`.

**What I learnt:** The final regional test achieved the best score of the project for this function, improving beyond the earlier local path.

**Code and data:** [Round notes](../../journey/round_13/README.md) · [Inputs](../../journey/round_13/queries.txt) · [Outputs](../../journey/round_13/outputs.txt) · [Final reflection](../../journey/final_reflection/README.md).

</details>

## Visual analysis

<table><tr><td width="50%"><img src="../../results/figures/f3_2d.svg" width="460" alt="Function 3 two-dimensional representation"></td><td width="50%"><img src="../../results/figures/f3_3d.svg" width="460" alt="Function 3 three-dimensional representation"></td></tr></table>

**Observed points only.** These 2D/3D views project the real inputs and their returned scores; no smooth objective surface has been invented. Only x1 and x2 appear on the horizontal axes; x3 varies across observations and the plots do not control for them.

[How the visualisations were produced](../../docs/functions.md) · [Graph-generation code](../../results/figures/build_visual_gallery.mjs)

## Mathematical evidence and its limits

**No validated hidden-function equation is available.** RBF and Matérn GPs, local fits and neural-network challengers are approximate predictive tools, not claims to know the underlying source. The observed maximum in the table is **a personal best**, not a proved global optimum.

## Lessons to carry forward

A smooth local curve and an accurate-looking mean can still select an unproductive region. Holdout evidence and alternative basins matter.


[← All eight functions](../README.md) · [Dataset description](../../DATASHEET.md) · [Model card](../../MODEL_CARD.md)

**Function navigation (3/8):** [← Previous: F2](../F2/README.md) · [All eight functions](../README.md) · [Next: F4 →](../F4/README.md)
