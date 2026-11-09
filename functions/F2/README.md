# Function 2: inputs, outputs and model evidence

**2 input dimensions · 10 starting observations · 13 submitted queries · best observed output `0.744250426302126`.**

F2's Round 9 local forecast failed; broader Round 13 searching improved the observed best.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.7-0.5` | `0.379063270240082` | `0.6112052158` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.672-0.999999` | `0.5860547049641637` | `0.6112052158` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.7015-0.957999` | `0.653867607133911` **↑** | `0.6538676071` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.705-0.999999` | `0.5912856598404541` | `0.6538676071` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.7015-0.959409` | `0.6548498709022528` **↑** | `0.6548498709` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.7015-0.959816` | `0.6913148663237587` **↑** | `0.6913148663` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.7015-0.960223` | `0.5893476079120687` | `0.6913148663` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.7015-0.95972` | `0.6130861312279376` | `0.6913148663` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.7015-0.959912` | `0.5055255161847483` | `0.6913148663` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.701500-0.959796` | `0.617259927400158` | `0.6913148663` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.692000-0.366000` | `0.6953368270741286` **↑** | `0.6953368271` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.684399-0.368552` | `0.660671151390024` | `0.6953368271` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.864900-0.500000` | `0.7442504263021256` **↑** | `0.7442504263` | [Evidence](../../journey/round_13/README.md) |

## Week-by-week development: actual inputs, outputs, strategy, code and lessons

Follow the same function from Round 1 to Round 13. The **portal input and output** are observed evidence, while the **lesson learnt** is retrospective interpretation. Strategy descriptions reproduce the available decision ledger; they do not assert that every related script generated the exact submitted point. Later structural reconstructions are never passed off as pre-result models. Read the table above for a compact results history, or use the sections below for the decision narrative.

### Round 1

**Submitted input:** `0.7-0.5`  
**Actual portal return:** `0.379063270240082`  
**Progress:** no new best; incumbent `0.611205216` retained.  
**Strategy evidence:** GP and acquisition baseline (retrospective).  
**Lesson learnt (retrospective):** An interior candidate scored below the starting best; central locations were not necessarily promising.  
**Source:** [round 1 evidence](../../journey/round_01/README.md) · Exact original selection script not retained.

### Round 2

**Submitted input:** `0.672-0.999999`  
**Actual portal return:** `0.5860547049641637`  
**Progress:** no new best; incumbent `0.611205216` retained.  
**Strategy evidence:** GP and UCB working package.  
**Lesson learnt (retrospective):** A wider query approached but did not exceed the incumbent.  
**Source:** [round 2 evidence](../../journey/round_02/README.md) · [related preserved code](../../journey/round_02/week2_ucb_course_aligned.py) (*related historical script not verified exact*).

### Round 3

**Submitted input:** `0.7015-0.957999`  
**Actual portal return:** `0.653867607133911`  
**Progress:** new best `0.6538676071` (previous `0.61120522`).  
**Strategy evidence:** Function-specific EI or wider search (retrospective).  
**Lesson learnt (retrospective):** Targeting a different region produced the first new personal best.  
**Source:** [round 3 evidence](../../journey/round_03/README.md) · Exact original selection script not retained.

### Round 4

**Submitted input:** `0.705-0.999999`  
**Actual portal return:** `0.5912856598404541`  
**Progress:** no new best; incumbent `0.653867607` retained.  
**Strategy evidence:** GP, SVM and neural-network diagnostics.  
**Lesson learnt (retrospective):** An upper-bound x2 move reduced performance; local continuity was questionable.  
**Source:** [round 4 evidence](../../journey/round_04/README.md) · [related preserved code](../../journey/round_04/capstone_bbo_week4_module15.py) (*related historical analysis not verified exact*).

### Round 5

**Submitted input:** `0.7015-0.959409`  
**Actual portal return:** `0.6548498709022528`  
**Progress:** new best `0.6548498709` (previous `0.65386761`).  
**Strategy evidence:** Controlled coordinate probes (retrospective).  
**Lesson learnt (retrospective):** A tiny x2 change improved the incumbent only slightly.  
**Source:** [round 5 evidence](../../journey/round_05/README.md) · Exact original selection script not retained.

### Round 6

**Submitted input:** `0.7015-0.959816`  
**Actual portal return:** `0.6913148663237587`  
**Progress:** new best `0.6913148663` (previous `0.65484987`).  
**Strategy evidence:** GP, ridge and MLP comparison; controlled local fit.  
**Lesson learnt (retrospective):** Another nearby probe yielded 0.691315; it did not establish global convergence.  
**Source:** [round 6 evidence](../../journey/round_06/README.md) · [related preserved code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) (*related notebook original fitter missing*).

### Round 7

**Submitted input:** `0.7015-0.960223`  
**Actual portal return:** `0.5893476079120687`  
**Progress:** no new best; incumbent `0.691314866` retained.  
**Strategy evidence:** ARD and local forecast investigations (retrospective).  
**Lesson learnt (retrospective):** Changing x2 by 0.000407 reduced the score sharply; the surface was difficult to forecast.  
**Source:** [round 7 evidence](../../journey/round_07/README.md) · Exact original selection script not retained.

### Round 8

**Submitted input:** `0.7015-0.95972`  
**Actual portal return:** `0.6130861312279376`  
**Progress:** no new best; incumbent `0.691314866` retained.  
**Strategy evidence:** Three-point local bracket around the Week 6 spike; quadratic vertex from x2=0.959409, 0.959816 and 0.960223 is approximately 0.959720..  
**Lesson learnt (retrospective):** Further nearby refinement missed the incumbent again.  
**Source:** [round 8 evidence](../../journey/round_08/README.md) · [related preserved code](../../journey/round_08/capstone_bbo_module19_round8.py) (*related historical analysis not verified exact*).

### Round 9

**Submitted input:** `0.7015-0.959912`  
**Actual portal return:** `0.5055255161847483`  
**Progress:** no new best; incumbent `0.691314866` retained.  
**Strategy evidence:** Symmetric local bracket around the Week 6 incumbent: Week 8 tested 0.000096 to the left, so Week 9 tests 0.000096 to the right. A local quadratic through Week 8, Week 6 and Week 7 predicts about 0.7305, but the main purpose is to map the very narrow peak..  
**Forecast recorded before outcome:** `0.7305023346561939`.  
**Lesson learnt (retrospective):** The saved forecast 0.730502 returned 0.505526; this was a decisive model warning.  
**Source:** [round 9 evidence](../../journey/round_09/README.md) · [related preserved code](../../journey/round_09/round9_controlled_fits.py) (*related historical analysis not verified exact*).

### Round 10

**Submitted input:** `0.701500-0.959796`  
**Actual portal return:** `0.617259927400158`  
**Progress:** no new best; incumbent `0.691314866` retained.  
**Strategy evidence:** Tight incumbent diagnostic after Week 9 GP forecast miss.  
**Lesson learnt (retrospective):** Another local candidate underperformed, supporting a search-policy change.  
**Source:** [round 10 evidence](../../journey/round_10/README.md) · [related preserved code](../../src/bbo/optimizer.py) (*related challenger not verified exact*).

### Round 11

**Submitted input:** `0.692000-0.366000`  
**Actual portal return:** `0.6953368270741286`  
**Progress:** new best `0.6953368271` (previous `0.69131487`).  
**Strategy evidence:** Alternative-region exploration and structural investigations.  
**Lesson learnt (retrospective):** A distinctly different region achieved 0.695337.  
**Source:** [round 11 evidence](../../journey/round_11/README.md) · Exact original selection script not retained.

### Round 12

**Submitted input:** `0.684399-0.368552`  
**Actual portal return:** `0.660671151390024`  
**Progress:** no new best; incumbent `0.695336827` retained.  
**Strategy evidence:** Controlled probes, repeats and structural investigations.  
**Lesson learnt (retrospective):** Refining its neighbourhood did not improve the best.  
**Source:** [round 12 evidence](../../journey/round_12/README.md) · Exact original selection script not retained.

### Round 13

**Submitted input:** `0.864900-0.500000`  
**Actual portal return:** `0.7442504263021256`  
**Progress:** new best `0.7442504263` (previous `0.69533683`).  
**Strategy evidence:** Final exploitation and regional probes.  
**Lesson learnt (retrospective):** Another competing region returned 0.744250; the apparent plateau was not final.  
**Source:** [round 13 evidence](../../journey/round_13/README.md) · Exact original selection script not retained.

## Per-function evidence

- [All observations](observations.csv): 10 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Preserved prospective forecasts

Recorded pre-result forecasts are distinguished from reconstructed estimates. Blank entries in the CSV mean no such numerical forecast was retained.

| Round | Recorded forecast | Actual result | Status |
|---:|---:|---:|---|
| 9 | `0.7305023346561939` | `0.5055255161847483` | recorded before return |

## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

No fully authenticated source equation is claimed for this function.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
