# Function 6 · Escaping an unstable local region

**Function navigation (6/8):** [← Previous: F5](../F5/README.md) · [All eight functions](../README.md) · [Next: F7 →](../F7/README.md)
[← All functions](../README.md) · [Project home](../../README.md) · [Observed inputs and outputs](observations.csv) · [Complete decision ledger](selection_history.csv)

**5 inputs · 20 starting observations · 13 rounds**

| Initial best | Final best | First achieved | Best input |
|---:|---:|:---:|---|
| `-0.7142649478202404` | **`-0.03751864724436928`** | **Round 12** | `0.415080-0.344119-0.644062-0.776818-0.076258` |

## Understanding this function

F6's negative response should be maximised towards zero. Close points initially gave surprisingly different results, causing local models and forecast intervals to lose credibility. Switching to an alternative region in R10 and subsequent refinement produced a much better best of -0.037519 in R12. No validated closed-form equation was established.

### Score progression from real evaluations

![Function 6 measured best-so-far history](progress.svg)

The chart tracks measured best-so-far results. A flat interval means no improvement to the incumbent, not that a model predicted a constant function.

## Weekly development · expand a round

<details>
<summary><strong>Round 1 · Opening hypothesis</strong> — -0.603980627 ★ new best</summary>

**Why this input:** Week 1 observed that raising selected coordinates and lowering another could help, and deliberately chose a relatively bold vector.

**Approach considered:** Manual exploration informed by the starting observations.

**Submitted input:** `0.440752-0.249118-0.839948-0.999999-1e-06`  
**Actual portal result:** `-0.6039806265819045`  
**Best observed before → after:** `-0.7142649478202404` → `-0.6039806265819045`.

**What I learnt:** The first input improved the initial best, but the response remained negative.

**Code and data:** [Round notes](../../journey/round_01/README.md) · [Inputs](../../journey/round_01/queries.txt) · [Outputs](../../journey/round_01/outputs.txt) · [Coursework notebook](../../journey/round_01/supporting_coursework/Required_assignment_12_1_Tamer_ready.ipynb).

</details>

<details>
<summary><strong>Round 2 · GP and UCB working package</strong> — -0.752987893</summary>

**Why this input:** The Week 1 result rose from -0.7143 to -0.6040, so Week 2 used UCB κ=1.0 with stronger exploitation and a high x4/low x5 hypothesis.

**Approach considered:** GP and UCB working package

**Submitted input:** `0.436716-0.004631-0.398416-0.895113-0.03487`  
**Actual portal result:** `-0.7529878928551597`  
**Best observed before → after:** `-0.6039806265819045` → `-0.6039806265819045`.

**What I learnt:** The GP/UCB candidate scored worse than the incumbent; more exploratory modelling did not guarantee progress.

**Code and data:** [Round notes](../../journey/round_02/README.md) · [Inputs](../../journey/round_02/queries.txt) · [Outputs](../../journey/round_02/outputs.txt) · [GP/UCB Python code](../../journey/round_02/week2_ucb_course_aligned.py) · [Saved candidates](../../journey/round_02/week2_ucb_results.csv) · [Notebook](../../journey/round_02/Capstone_BBO_Week2_UCB_only.ipynb).

</details>

<details>
<summary><strong>Round 3 · Function-specific EI or wider search</strong> — -0.569779050 ★ new best</summary>

**Why this input:** The early Week 3 local-EI policy followed the stronger observed region but did not yet establish coordinate-wise causality.

**Approach considered:** Function-specific EI or wider search

**Submitted input:** `0.467823-0.254239-0.82281-0.999999-0.03819`  
**Actual portal result:** `-0.5697790503980307`  
**Best observed before → after:** `-0.6039806265819045` → `-0.5697790503980307`.

**What I learnt:** A different candidate improved the best score, warranting further regional tests.

**Code and data:** [Round notes](../../journey/round_03/README.md) · [Inputs](../../journey/round_03/queries.txt) · [Outputs](../../journey/round_03/outputs.txt).

</details>

<details>
<summary><strong>Round 4 · GP, SVM and neural-network diagnostics</strong> — -0.541447832 ★ new best</summary>

**Why this input:** Fourth round: GP paired with SVM good/bad checks and small neural-network gradient challengers, not hard classifier exclusion.

**Approach considered:** GP, SVM and neural-network diagnostics

**Submitted input:** `0.481359-0.2568-0.814241-0.999999-0.057285`  
**Actual portal result:** `-0.5414478319707962`  
**Best observed before → after:** `-0.5697790503980307` → `-0.5414478319707962`.

**What I learnt:** The new input raised the incumbent to about −0.541448, but local behaviour remained difficult.

**Code and data:** [Round notes](../../journey/round_04/README.md) · [Inputs](../../journey/round_04/queries.txt) · [Outputs](../../journey/round_04/outputs.txt) · [Python analysis](../../journey/round_04/capstone_bbo_week4_module15.py) · [Notebook](../../journey/round_04/Capstone_BBO_Week4_Module15.ipynb).

</details>

<details>
<summary><strong>Round 5 · Controlled coordinate probes</strong> — -0.572992776</summary>

**Why this input:** Round 4 raised the best to approximately −0.541448. I tested a further controlled move along the same local direction.

**Approach considered:** Controlled coordinate probes

**Submitted input:** `0.494895-0.259361-0.805672-0.999999-0.07638`  
**Actual portal result:** `-0.5729927758567235`  
**Best observed before → after:** `-0.5414478319707962` → `-0.5414478319707962`.

**What I learnt:** Continuing the controlled direction produced a lower score, weakening a simple monotonic interpretation.

**Code and data:** [Round notes](../../journey/round_05/README.md) · [Inputs](../../journey/round_05/queries.txt) · [Outputs](../../journey/round_05/outputs.txt).

</details>

<details>
<summary><strong>Round 6 · GP, ridge and MLP comparison; controlled local fit</strong> — -0.698029551</summary>

**Why this input:** I compared GP and small-MLP fits, then tested how accurately the local model predicted another candidate.

**Approach considered:** GP, ridge and MLP comparison; controlled local fit

**Submitted input:** `0.480996-0.256731-0.814471-0.999999-0.056773`  
**Actual portal result:** `-0.6980295508727566`  
**Best observed before → after:** `-0.5414478319707962` → `-0.5414478319707962`.

**What I learnt:** The prediction was substantially too optimistic: the portal returned about −0.698 rather than the expected −0.562.

**Code and data:** [Round notes](../../journey/round_06/README.md) · [Inputs](../../journey/round_06/queries.txt) · [Outputs](../../journey/round_06/outputs.txt) · [Notebook](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) · [Eight selected inputs](../../journey/round_06/results/round6_queries.csv) · [Decision notes](../../journey/round_06/results/round6_query_rationale.csv).

</details>

<details>
<summary><strong>Round 7 · ARD and local forecast investigations</strong> — -0.590379290</summary>

**Why this input:** After that failure, the original Week 7 plan explicitly tested near the incumbent rather than make another large model-led jump.

**Approach considered:** ARD and local forecast investigations

**Submitted input:** `0.48136-0.2568-0.814241-0.999999-0.057285`  
**Actual portal result:** `-0.5903792900833394`  
**Best observed before → after:** `-0.5414478319707962` → `-0.5414478319707962`.

**What I learnt:** A near-incumbent test did not exceed the best, so local stability still needed investigation.

**Code and data:** [Round notes](../../journey/round_07/README.md) · [Inputs](../../journey/round_07/queries.txt) · [Outputs](../../journey/round_07/outputs.txt) · [Forecast comparison](../../journey/round_08/results/week7_audit.csv).

</details>

<details>
<summary><strong>Round 8 · Testing the sensitivity of x1</strong> — -0.633781715</summary>

**Why this input:** Original late-week notes treated tiny perturbations as a local stability test, not proof of a smooth gradient.

**Approach:** Week 7 changed x1 by only +0.000001 from the Week 4 incumbent but lost about 0.049. Test the symmetric -0.000001 side to distinguish a razor-sharp local feature from instability/noise.

**Submitted input:** `0.481358-0.2568-0.814241-0.999999-0.057285`  
**Actual portal result:** `-0.6337817154897656`  
**Best observed before → after:** `-0.5414478319707962` → `-0.5414478319707962`.

**What I learnt:** The tiny x1 perturbation produced a noticeably worse score, exposing sharp local sensitivity.

**Code and data:** [Round notes](../../journey/round_08/README.md) · [Inputs](../../journey/round_08/queries.txt) · [Outputs](../../journey/round_08/outputs.txt) · [Python analysis](../../journey/round_08/capstone_bbo_module19_round8.py) · [Saved candidates](../../journey/round_08/results/round8_queries.csv).

</details>

<details>
<summary><strong>Round 9 · Holding x1 while testing a small x5 change</strong> — -0.551286448</summary>

**Why this input:** The Week 9 paper noted that F6 needed a stability test around an unusually sharp incumbent.

**Approach:** Hold the razor-sharp x1 incumbent exactly and move only x5 by +0.000001. This tests whether the Week 4 high value lies on a narrow ridge rather than repeating the same point.

**Submitted input:** `0.481359-0.2568-0.814241-0.999999-0.057286`  
**Actual portal result:** `-0.5512864477685001`  
**Best observed before → after:** `-0.5414478319707962` → `-0.5414478319707962`.

**What I learnt:** Adjusting x5 while holding the sharp x1 setting did not improve the incumbent.

**Code and data:** [Round notes](../../journey/round_09/README.md) · [Inputs](../../journey/round_09/queries.txt) · [Outputs](../../journey/round_09/outputs.txt) · [Candidate forecasts](../../journey/round_09/results/round9_queries.csv).

</details>

<details>
<summary><strong>Round 10 · Peer-informed GP regional exploration; model forecast only</strong> — -0.285656144 ★ new best</summary>

**Why this input:** The Round 10 plan investigated a peer-informed GP model and competing region, with predicted mean -0.192 against -0.262 for the older proposal; neither forecast was an observed result.

**Approach:** Peer-informed GP regional exploration; model forecast only.

**Submitted input:** `0.379322-0.338275-0.586412-0.727790-0.036539`  
**Actual portal result:** `-0.28565614419980845`  
**Best observed before → after:** `-0.5414478319707962` → `-0.28565614419980845`.

**What I learnt:** A different region returned about −0.285656, a material improvement over the unstable neighbourhood.

**Code and data:** [Round notes](../../journey/round_10/README.md) · [Inputs](../../journey/round_10/queries.txt) · [Outputs](../../journey/round_10/outputs.txt) · [Candidate list](../../journey/round_10/round10_candidates.csv) · [Search plan](../../journey/round_10/optimisation.yaml) · [Related optimiser code](../../src/bbo/optimizer.py).

</details>

<details>
<summary><strong>Round 11 · Refining the alternative region</strong> — -0.123761480 ★ new best</summary>

**Why this input:** An alternative point continued a useful trajectory away from the earlier unstable neighbourhood.

**Approach:** Explore a stronger region.

**Submitted input:** `0.457000-0.370000-0.642000-0.738000-0.020000`  
**Actual portal result:** `-0.12376148016289273`  
**Best observed before → after:** `-0.28565614419980845` → `-0.12376148016289273`.

**What I learnt:** A further candidate in the new region improved the score to about −0.123761.

**Code and data:** [Round notes](../../journey/round_11/README.md) · [Portal results](../../data/portal_rounds_11_12.csv) · [Clustering analysis (later reproduction)](../../research/diagnostics/clustering/clustering_audit.py).

</details>

<details>
<summary><strong>Round 12 · Multi-coordinate refinement to the best score</strong> — -0.0375186472 ★ new best</summary>

**Why this input:** Following the Round 11 improvement, I varied several coordinates together to investigate the new promising region.

**Approach:** Multi-coordinate refinement.

**Submitted input:** `0.415080-0.344119-0.644062-0.776818-0.076258`  
**Actual portal result:** `-0.03751864724436928`  
**Best observed before → after:** `-0.12376148016289273` → `-0.03751864724436928`.

**What I learnt:** A multi-coordinate refinement reached about −0.037519, the best recorded result for this function.

**Code and data:** [Round notes](../../journey/round_12/README.md) · [Round 12 Python](../../journey/round_12/original/review_round12.py) · [Robustness code](../../journey/round_12/original/robust_and_warp.py) · [Trust-region and Thompson-sampling code](../../journey/round_12/original/trust_region_ts.py) · [Candidate rationale](../../journey/round_12/original/week12_full_review_2026-11-02.md).

</details>

<details>
<summary><strong>Round 13 · Testing the new best region</strong> — -0.0769802870</summary>

**Why this input:** Round 12 had improved the best to approximately −0.037519. I tested a nearby but distinct vector in the final evaluation.

**Approach:** Final nearby sensitivity test.

**Submitted input:** `0.420000-0.360000-0.650000-0.770000-0.100000`  
**Actual portal result:** `-0.07698028695699928`  
**Best observed before → after:** `-0.03751864724436928` → `-0.03751864724436928`.

**What I learnt:** The last query scored below the Round 12 best; the final result is not the final incumbent.

**Code and data:** [Round notes](../../journey/round_13/README.md) · [Inputs](../../journey/round_13/queries.txt) · [Outputs](../../journey/round_13/outputs.txt) · [Final reflection](../../journey/final_reflection/README.md).

</details>

## Visual analysis

<table><tr><td width="50%"><img src="../../results/figures/f6_2d.svg" width="460" alt="Function 6 two-dimensional representation"></td><td width="50%"><img src="../../results/figures/f6_3d.svg" width="460" alt="Function 6 three-dimensional representation"></td></tr></table>

**Observed points only.** These 2D/3D views project the real inputs and their returned scores; no smooth objective surface has been invented. Only x1 and x2 appear on the horizontal axes; x3–x5 vary across observations and the plots do not control for them.

[How the visualisations were produced](../../docs/functions.md) · [Graph-generation code](../../results/figures/build_visual_gallery.mjs)

## Mathematical evidence and its limits

**No validated hidden-function equation is available.** RBF and Matérn GPs, local fits and neural-network challengers are approximate predictive tools, not claims to know the underlying source. The observed maximum in the table is **a personal best**, not a proved global optimum.

## Lessons to carry forward

Repeatedly fitting a local model does not fix a locally unreliable response. Change region or representation when forecasts and nearby probes consistently disagree.


[← All eight functions](../README.md) · [Dataset description](../../DATASHEET.md) · [Model card](../../MODEL_CARD.md)

**Function navigation (6/8):** [← Previous: F5](../F5/README.md) · [All eight functions](../README.md) · [Next: F7 →](../F7/README.md)
