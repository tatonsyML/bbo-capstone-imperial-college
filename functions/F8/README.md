# Function 8: inputs, outputs and model evidence

**8 input dimensions · 40 starting observations · 13 submitted queries · best observed output `10.0000000000000`.**

F8's additive quadratic led to a Round 10 portal-confirmed value of ten. Independent 40/13 validation was performed later.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.088526-0.03196-0.048494-0.063991-0.991333-0.224689-0.073759-0.537568` | `9.8321123600691` **↑** | `9.832112360` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.321822-0.045429-0.355724-0.015612-0.965914-0.090106-0.138377-0.028859` | `9.4977489881389` | `9.832112360` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.099253-0.051531-0.055571-0.074437-0.985751-0.228722-0.118577-0.53735` | `9.8634785625365` **↑** | `9.863478563` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.104617-0.061316-0.05911-0.07966-0.98296-0.230739-0.140986-0.537241` | `9.8754707823449` **↑** | `9.875470782` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.109981-0.071101-0.062649-0.084883-0.980169-0.232756-0.163395-0.537132` | `9.8850021313761` **↑** | `9.885002131` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.115345-0.080886-0.066188-0.090106-0.977378-0.234773-0.185804-0.537023` | `9.8920726096301` **↑** | `9.892072610` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.128076-0.104109-0.074587-0.102502-0.970754-0.23956-0.238989-0.536764` | `9.8990020095864` **↑** | `9.899002010` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.128076-0.104109-0.074587-0.102502-0.970754-0.26456-0.238989-0.536764` | `9.9113990095864` **↑** | `9.911399010` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.128076-0.104109-0.074587-0.102502-0.970754-0.31456-0.238989-0.536764` | `9.9324430095864` **↑** | `9.932443010` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000` | `10` **↑** | `10.00000000` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000` | `10` | `10.00000000` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000` | `10` | `10.00000000` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000` | `10` | `10.00000000` | [Evidence](../../journey/round_13/README.md) |

## Week-by-week development: actual inputs, outputs, strategy, code and lessons

Follow the same function from Round 1 to Round 13. The **portal input and output** are observed evidence, while the **lesson learnt** is retrospective interpretation. Strategy descriptions reproduce the available decision ledger; they do not assert that every related script generated the exact submitted point. Later structural reconstructions are never passed off as pre-result models. Read the table above for a compact results history, or use the sections below for the decision narrative.

### Round 1

**Submitted input:** `0.088526-0.03196-0.048494-0.063991-0.991333-0.224689-0.073759-0.537568`  
**Actual portal return:** `9.8321123600691`  
**Progress:** new best `9.832112360` (previous `9.5984820`).  
**Strategy evidence:** GP and acquisition baseline (retrospective).  
**Lesson learnt (retrospective):** The first GP-guided candidate improved the incumbent.  
**Source:** [round 1 evidence](../../journey/round_01/README.md) · Exact original selection script not retained.

### Round 2

**Submitted input:** `0.321822-0.045429-0.355724-0.015612-0.965914-0.090106-0.138377-0.028859`  
**Actual portal return:** `9.4977489881389`  
**Progress:** no new best; incumbent `9.83211236` retained.  
**Strategy evidence:** GP and UCB working package.  
**Lesson learnt (retrospective):** Broad eight-dimensional exploration underperformed.  
**Source:** [round 2 evidence](../../journey/round_02/README.md) · [related preserved code](../../journey/round_02/week2_ucb_course_aligned.py) (*related historical script not verified exact*).

### Round 3

**Submitted input:** `0.099253-0.051531-0.055571-0.074437-0.985751-0.228722-0.118577-0.53735`  
**Actual portal return:** `9.8634785625365`  
**Progress:** new best `9.863478563` (previous `9.8321124`).  
**Strategy evidence:** Function-specific EI or wider search (retrospective).  
**Lesson learnt (retrospective):** A more targeted input established a new best.  
**Source:** [round 3 evidence](../../journey/round_03/README.md) · Exact original selection script not retained.

### Round 4

**Submitted input:** `0.104617-0.061316-0.05911-0.07966-0.98296-0.230739-0.140986-0.537241`  
**Actual portal return:** `9.8754707823449`  
**Progress:** new best `9.875470782` (previous `9.8634786`).  
**Strategy evidence:** GP, SVM and neural-network diagnostics.  
**Lesson learnt (retrospective):** Local refinement improved further.  
**Source:** [round 4 evidence](../../journey/round_04/README.md) · [related preserved code](../../journey/round_04/capstone_bbo_week4_module15.py) (*related historical analysis not verified exact*).

### Round 5

**Submitted input:** `0.109981-0.071101-0.062649-0.084883-0.980169-0.232756-0.163395-0.537132`  
**Actual portal return:** `9.8850021313761`  
**Progress:** new best `9.885002131` (previous `9.8754708`).  
**Strategy evidence:** Controlled coordinate probes (retrospective).  
**Lesson learnt (retrospective):** Another controlled step raised the score.  
**Source:** [round 5 evidence](../../journey/round_05/README.md) · Exact original selection script not retained.

### Round 6

**Submitted input:** `0.115345-0.080886-0.066188-0.090106-0.977378-0.234773-0.185804-0.537023`  
**Actual portal return:** `9.8920726096301`  
**Progress:** new best `9.892072610` (previous `9.8850021`).  
**Strategy evidence:** GP, ridge and MLP comparison; controlled local fit.  
**Lesson learnt (retrospective):** The next step reached 9.892073; its forecast was within about 0.000025.  
**Source:** [round 6 evidence](../../journey/round_06/README.md) · [related preserved code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) (*related notebook original fitter missing*).

### Round 7

**Submitted input:** `0.128076-0.104109-0.074587-0.102502-0.970754-0.23956-0.238989-0.536764`  
**Actual portal return:** `9.8990020095864`  
**Progress:** new best `9.899002010` (previous `9.8920726`).  
**Strategy evidence:** ARD and local forecast investigations (retrospective).  
**Lesson learnt (retrospective):** Progress along the tested trajectory continued.  
**Source:** [round 7 evidence](../../journey/round_07/README.md) · Exact original selection script not retained.

### Round 8

**Submitted input:** `0.128076-0.104109-0.074587-0.102502-0.970754-0.26456-0.238989-0.536764`  
**Actual portal return:** `9.9113990095864`  
**Progress:** new best `9.911399010` (previous `9.8990020`).  
**Strategy evidence:** Week 7 landed essentially exactly on the validated trajectory vertex. Leave that path fixed and test one orthogonal coordinate: increase x6 by 0.025, where the GP-kernel committee agrees on positive headroom..  
**Lesson learnt (retrospective):** Increasing x6 alone produced a measured gain.  
**Source:** [round 8 evidence](../../journey/round_08/README.md) · [related preserved code](../../journey/round_08/capstone_bbo_module19_round8.py) (*related historical analysis not verified exact*).

### Round 9

**Submitted input:** `0.128076-0.104109-0.074587-0.102502-0.970754-0.31456-0.238989-0.536764`  
**Actual portal return:** `9.9324430095864`  
**Progress:** new best `9.932443010` (previous `9.9113990`).  
**Strategy evidence:** Continue the newly validated x6 direction with a +0.05 step. Three GP kernels fitted after Week 8 agree on improvement; their mean forecast is about 9.9335..  
**Forecast recorded before outcome:** `9.933511308824693`.  
**Lesson learnt (retrospective):** A further x6 increase produced 9.932443.  
**Source:** [round 9 evidence](../../journey/round_09/README.md) · [related preserved code](../../journey/round_09/round9_controlled_fits.py) (*related historical analysis not verified exact*).

### Round 10

**Submitted input:** `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000`  
**Actual portal return:** `10`  
**Progress:** new best `10.00000000` (previous `9.9324430`).  
**Strategy evidence:** 17-coefficient additive quadratic fitted vertex; predicted score 10.  
**Forecast recorded before outcome:** `10`.  
**Lesson learnt (retrospective):** The fitted 17-coefficient quadratic predicted 10 at its vertex; the portal confirmed it.  
**Source:** [round 10 evidence](../../journey/round_10/README.md) · [related preserved code](../../src/bbo/optimizer.py) (*related challenger not verified exact*).

### Round 11

**Submitted input:** `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000`  
**Actual portal return:** `10`  
**Progress:** no new best; incumbent `10.0000000` retained.  
**Strategy evidence:** Alternative-region exploration and structural investigations.  
**Lesson learnt (retrospective):** The analytic vertex was deliberately repeated, not perturbed.  
**Source:** [round 11 evidence](../../journey/round_11/README.md) · Exact original selection script not retained.

### Round 12

**Submitted input:** `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000`  
**Actual portal return:** `10`  
**Progress:** no new best; incumbent `10.0000000` retained.  
**Strategy evidence:** Controlled probes, repeats and structural investigations.  
**Lesson learnt (retrospective):** Repeating the optimum confirmed the return but supplied no new neighbourhood evidence.  
**Source:** [round 12 evidence](../../journey/round_12/README.md) · Exact original selection script not retained.

### Round 13

**Submitted input:** `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000`  
**Actual portal return:** `10`  
**Progress:** no new best; incumbent `10.0000000` retained.  
**Strategy evidence:** Final exploitation and regional probes.  
**Lesson learnt (retrospective):** The final input retained the vertex; there was no credible improvement within the validated quadratic.  
**Source:** [round 13 evidence](../../journey/round_13/README.md) · Exact original selection script not retained.

## Per-function evidence

- [All observations](observations.csv): 40 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Preserved prospective forecasts

Recorded pre-result forecasts are distinguished from reconstructed estimates. Blank entries in the CSV mean no such numerical forecast was retained.

| Round | Recorded forecast | Actual result | Status |
|---:|---:|---:|---|
| 9 | `9.933511308824693` | `9.9324430095864` | recorded before return |
| 10 | `10` | `10` | recorded structural prediction before return |

## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

[F8 structural validation](../../src/bbo/structural_validation.py) retrospectively fits the initial 40 points and validates against 13 later outcomes. This fit was not performed in Round 1.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
