# Function 3: inputs, outputs and model evidence

**3 input dimensions · 15 starting observations · 13 submitted queries · best observed output `-0.00375309691871926`.**

Negative scores, local paths and alternative regions tested the limits of an assumed smooth surrogate.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.5-0.5-0.345` | `-0.0437772384849064` | `-0.03483531335` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.993188-0.591985-0.00028` | `-0.1064950977729621` | `-0.03483531335` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.496377-0.564413-0.34369` | `-0.0427365723752823` | `-0.03483531335` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.49-0.62-0.36` | `-0.0312815968234451` **↑** | `-0.03128159682` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.483623-0.675587-0.37631` | `-0.0334231088352711` | `-0.03128159682` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.487816-0.639038-0.365586` | `-0.0208561545295093` **↑** | `-0.02085615453` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.486949-0.646592-0.367803` | `-0.0279111486430777` | `-0.02085615453` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.488344-0.634434-0.364235` | `-0.0296632773887996` | `-0.02085615453` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.487611-0.640821-0.366109` | `-0.0258164064206346` | `-0.02085615453` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.469634-0.620072-0.416672` | `-0.014602810625106634` **↑** | `-0.01460281063` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.445500-0.593000-0.420000` | `-0.005709220275560069` **↑** | `-0.005709220276` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.313581-0.474345-0.485191` | `-0.0226526646178297` | `-0.005709220276` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.197280-0.523429-0.470094` | `-0.0037530969187192596` **↑** | `-0.003753096919` | [Evidence](../../journey/round_13/README.md) |

## Week-by-week development: actual inputs, outputs, strategy, code and lessons

Follow the same function from Round 1 to Round 13. The **portal input and output** are observed evidence, while the **lesson learnt** is retrospective interpretation. Strategy descriptions reproduce the available decision ledger; they do not assert that every related script generated the exact submitted point. Later structural reconstructions are never passed off as pre-result models. Read the table above for a compact results history, or use the sections below for the decision narrative.

### Round 1

**Submitted input:** `0.5-0.5-0.345`  
**Actual portal return:** `-0.0437772384849064`  
**Progress:** no new best; incumbent `-0.0348353134` retained.  
**Strategy evidence:** GP and acquisition baseline (retrospective).  
**Lesson learnt (retrospective):** The initial query underperformed the original best.  
**Source:** [round 1 evidence](../../journey/round_01/README.md) · Exact original selection script not retained.

### Round 2

**Submitted input:** `0.993188-0.591985-0.00028`  
**Actual portal return:** `-0.1064950977729621`  
**Progress:** no new best; incumbent `-0.0348353134` retained.  
**Strategy evidence:** GP and UCB working package.  
**Lesson learnt (retrospective):** A boundary-oriented proposal performed substantially worse.  
**Source:** [round 2 evidence](../../journey/round_02/README.md) · [related preserved code](../../journey/round_02/week2_ucb_course_aligned.py) (*related historical script not verified exact*).

### Round 3

**Submitted input:** `0.496377-0.564413-0.34369`  
**Actual portal return:** `-0.0427365723752823`  
**Progress:** no new best; incumbent `-0.0348353134` retained.  
**Strategy evidence:** Function-specific EI or wider search (retrospective).  
**Lesson learnt (retrospective):** A more central point improved on the last response but not the incumbent.  
**Source:** [round 3 evidence](../../journey/round_03/README.md) · Exact original selection script not retained.

### Round 4

**Submitted input:** `0.49-0.62-0.36`  
**Actual portal return:** `-0.0312815968234451`  
**Progress:** new best `-0.03128159682` (previous `-0.034835313`).  
**Strategy evidence:** GP, SVM and neural-network diagnostics.  
**Lesson learnt (retrospective):** A target-region probe finally raised the best to -0.031282.  
**Source:** [round 4 evidence](../../journey/round_04/README.md) · [related preserved code](../../journey/round_04/capstone_bbo_week4_module15.py) (*related historical analysis not verified exact*).

### Round 5

**Submitted input:** `0.483623-0.675587-0.37631`  
**Actual portal return:** `-0.0334231088352711`  
**Progress:** no new best; incumbent `-0.0312815968` retained.  
**Strategy evidence:** Controlled coordinate probes (retrospective).  
**Lesson learnt (retrospective):** The next refinement lost ground; the local direction was not consistent.  
**Source:** [round 5 evidence](../../journey/round_05/README.md) · Exact original selection script not retained.

### Round 6

**Submitted input:** `0.487816-0.639038-0.365586`  
**Actual portal return:** `-0.0208561545295093`  
**Progress:** new best `-0.02085615453` (previous `-0.031281597`).  
**Strategy evidence:** GP, ridge and MLP comparison; controlled local fit.  
**Lesson learnt (retrospective):** A different local candidate improved to -0.020856.  
**Source:** [round 6 evidence](../../journey/round_06/README.md) · [related preserved code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) (*related notebook original fitter missing*).

### Round 7

**Submitted input:** `0.486949-0.646592-0.367803`  
**Actual portal return:** `-0.0279111486430777`  
**Progress:** no new best; incumbent `-0.0208561545` retained.  
**Strategy evidence:** ARD and local forecast investigations (retrospective).  
**Lesson learnt (retrospective):** The next trial regressed, weakening a smooth trajectory assumption.  
**Source:** [round 7 evidence](../../journey/round_07/README.md) · Exact original selection script not retained.

### Round 8

**Submitted input:** `0.488344-0.634434-0.364235`  
**Actual portal return:** `-0.0296632773887996`  
**Progress:** no new best; incumbent `-0.0208561545` retained.  
**Strategy evidence:** Week 7 overshot the Week 6 local best. A quadratic through the left bracket, Week 6 best and Week 7 point places the local vertex back at t≈0.260 on the controlled path..  
**Lesson learnt (retrospective):** A quadratic-bracket proposal also failed to improve.  
**Source:** [round 8 evidence](../../journey/round_08/README.md) · [related preserved code](../../journey/round_08/capstone_bbo_module19_round8.py) (*related historical analysis not verified exact*).

### Round 9

**Submitted input:** `0.487611-0.640821-0.366109`  
**Actual portal return:** `-0.0258164064206346`  
**Progress:** no new best; incumbent `-0.0208561545` retained.  
**Strategy evidence:** Updated local-path quadratic using Week 8, Week 6 and Week 7 places the vertex near this point, predicting about -0.02011. This is a tighter bracket after two forecast misses..  
**Forecast recorded before outcome:** `-0.02011192237870145`.  
**Lesson learnt (retrospective):** Another fitted local candidate missed its predicted improvement.  
**Source:** [round 9 evidence](../../journey/round_09/README.md) · [related preserved code](../../journey/round_09/round9_controlled_fits.py) (*related historical analysis not verified exact*).

### Round 10

**Submitted input:** `0.469634-0.620072-0.416672`  
**Actual portal return:** `-0.014602810625106634`  
**Progress:** new best `-0.01460281063` (previous `-0.020856155`).  
**Strategy evidence:** Alternative-region local interpolation; external evidence; uncertain.  
**Lesson learnt (retrospective):** Alternative regional evidence supported a new best at -0.014603.  
**Source:** [round 10 evidence](../../journey/round_10/README.md) · [related preserved code](../../src/bbo/optimizer.py) (*related challenger not verified exact*).

### Round 11

**Submitted input:** `0.445500-0.593000-0.420000`  
**Actual portal return:** `-0.005709220275560069`  
**Progress:** new best `-0.005709220276` (previous `-0.014602811`).  
**Strategy evidence:** Alternative-region exploration and structural investigations.  
**Lesson learnt (retrospective):** A further region improved to -0.005709.  
**Source:** [round 11 evidence](../../journey/round_11/README.md) · Exact original selection script not retained.

### Round 12

**Submitted input:** `0.313581-0.474345-0.485191`  
**Actual portal return:** `-0.0226526646178297`  
**Progress:** no new best; incumbent `-0.00570922028` retained.  
**Strategy evidence:** Controlled probes, repeats and structural investigations.  
**Lesson learnt (retrospective):** An exploratory test moved away from the strongest region.  
**Source:** [round 12 evidence](../../journey/round_12/README.md) · Exact original selection script not retained.

### Round 13

**Submitted input:** `0.197280-0.523429-0.470094`  
**Actual portal return:** `-0.0037530969187192596`  
**Progress:** new best `-0.003753096919` (previous `-0.0057092203`).  
**Strategy evidence:** Final exploitation and regional probes.  
**Lesson learnt (retrospective):** The final competing region gave -0.003753, the highest observed value.  
**Source:** [round 13 evidence](../../journey/round_13/README.md) · Exact original selection script not retained.

## Per-function evidence

- [All observations](observations.csv): 15 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Preserved prospective forecasts

Recorded pre-result forecasts are distinguished from reconstructed estimates. Blank entries in the CSV mean no such numerical forecast was retained.

| Round | Recorded forecast | Actual result | Status |
|---:|---:|---:|---|
| 9 | `-0.02011192237870145` | `-0.0258164064206346` | recorded before return |

## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

No fully authenticated source equation is claimed for this function.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
