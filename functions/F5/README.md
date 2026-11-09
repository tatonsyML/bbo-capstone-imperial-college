# Function 5: inputs, outputs and model evidence

**4 input dimensions · 20 starting observations · 13 submitted queries · best observed output `8662.40500124830`.**

Measured boundary changes culminated in a Round 10 legal-upper-corner improvement.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.1-0.75-0.9-0.98` | `1426.0897645116545` **↑** | `1426.089765` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.522156-0.922246-0.999259-0.99589` | `3722.27447382346` **↑** | `3722.274474` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.508373-0.970147-0.999999-0.999999` | `4295.86773060836` **↑** | `4295.867731` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.508373-0.999999-0.999999-0.999999` | `4694.317308235808` **↑** | `4694.317308` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.558373-0.999999-0.999999-0.999999` | `4807.986076589498` **↑** | `4807.986077` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.608373-0.999999-0.999999-0.999999` | `4957.571711515816` **↑** | `4957.571712` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.658373-0.999999-0.999999-0.999999` | `5151.047725485012` **↑** | `5151.047725` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.758373-0.999999-0.999999-0.999999` | `5709.3613198927205` **↑** | `5709.361320` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.858373-0.999999-0.999999-0.999999` | `6583.56144525802` **↑** | `6583.561445` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.999999-0.999999-0.999999-0.999999` | `8662.405001248297` **↑** | `8662.405001` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.999999-0.999999-0.999999-0.999999` | `8662.405001248297` | `8662.405001` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.999999-0.999999-0.999999-0.999999` | `8662.405001248297` | `8662.405001` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.999999-0.999999-0.999999-0.999999` | `8662.405001248297` | `8662.405001` | [Evidence](../../journey/round_13/README.md) |

## Week-by-week development: actual inputs, outputs, strategy, code and lessons

Follow the same function from Round 1 to Round 13. The **portal input and output** are observed evidence, while the **lesson learnt** is retrospective interpretation. Strategy descriptions reproduce the available decision ledger; they do not assert that every related script generated the exact submitted point. Later structural reconstructions are never passed off as pre-result models. Read the table above for a compact results history, or use the sections below for the decision narrative.

### Round 1

**Submitted input:** `0.1-0.75-0.9-0.98`  
**Actual portal return:** `1426.0897645116545`  
**Progress:** new best `1426.089765` (previous `1088.8596`).  
**Strategy evidence:** GP and acquisition baseline (retrospective).  
**Lesson learnt (retrospective):** A first selected point established a higher best.  
**Source:** [round 1 evidence](../../journey/round_01/README.md) · Exact original selection script not retained.

### Round 2

**Submitted input:** `0.522156-0.922246-0.999259-0.99589`  
**Actual portal return:** `3722.27447382346`  
**Progress:** new best `3722.274474` (previous `1426.0898`).  
**Strategy evidence:** GP and UCB working package.  
**Lesson learnt (retrospective):** The next query rose sharply to 3722.274, showing strong upper-coordinate potential.  
**Source:** [round 2 evidence](../../journey/round_02/README.md) · [related preserved code](../../journey/round_02/week2_ucb_course_aligned.py) (*related historical script not verified exact*).

### Round 3

**Submitted input:** `0.508373-0.970147-0.999999-0.999999`  
**Actual portal return:** `4295.86773060836`  
**Progress:** new best `4295.867731` (previous `3722.2745`).  
**Strategy evidence:** Function-specific EI or wider search (retrospective).  
**Lesson learnt (retrospective):** Further movement towards the boundary returned 4295.868.  
**Source:** [round 3 evidence](../../journey/round_03/README.md) · Exact original selection script not retained.

### Round 4

**Submitted input:** `0.508373-0.999999-0.999999-0.999999`  
**Actual portal return:** `4694.317308235808`  
**Progress:** new best `4694.317308` (previous `4295.8677`).  
**Strategy evidence:** GP, SVM and neural-network diagnostics.  
**Lesson learnt (retrospective):** Increasing x2 alone to its legal upper bound returned 4694.317.  
**Source:** [round 4 evidence](../../journey/round_04/README.md) · [related preserved code](../../journey/round_04/capstone_bbo_week4_module15.py) (*related historical analysis not verified exact*).

### Round 5

**Submitted input:** `0.558373-0.999999-0.999999-0.999999`  
**Actual portal return:** `4807.986076589498`  
**Progress:** new best `4807.986077` (previous `4694.3173`).  
**Strategy evidence:** Controlled coordinate probes (retrospective).  
**Lesson learnt (retrospective):** Increasing x1 with other coordinates fixed returned 4807.986.  
**Source:** [round 5 evidence](../../journey/round_05/README.md) · Exact original selection script not retained.

### Round 6

**Submitted input:** `0.608373-0.999999-0.999999-0.999999`  
**Actual portal return:** `4957.571711515816`  
**Progress:** new best `4957.571712` (previous `4807.9861`).  
**Strategy evidence:** GP, ridge and MLP comparison; controlled local fit.  
**Lesson learnt (retrospective):** Another controlled x1 increase made a further gain.  
**Source:** [round 6 evidence](../../journey/round_06/README.md) · [related preserved code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) (*related notebook original fitter missing*).

### Round 7

**Submitted input:** `0.658373-0.999999-0.999999-0.999999`  
**Actual portal return:** `5151.047725485012`  
**Progress:** new best `5151.047725` (previous `4957.5717`).  
**Strategy evidence:** ARD and local forecast investigations (retrospective).  
**Lesson learnt (retrospective):** The monotonic x1 trend continued.  
**Source:** [round 7 evidence](../../journey/round_07/README.md) · Exact original selection script not retained.

### Round 8

**Submitted input:** `0.758373-0.999999-0.999999-0.999999`  
**Actual portal return:** `5709.3613198927205`  
**Progress:** new best `5709.361320` (previous `5151.0477`).  
**Strategy evidence:** The controlled x1 series remains monotonic with accelerating gains. Increase x1 by 0.10 while retaining x2-x4 at the validated upper boundary..  
**Lesson learnt (retrospective):** A larger x1 step yielded a larger absolute gain.  
**Source:** [round 8 evidence](../../journey/round_08/README.md) · [related preserved code](../../journey/round_08/capstone_bbo_module19_round8.py) (*related historical analysis not verified exact*).

### Round 9

**Submitted input:** `0.858373-0.999999-0.999999-0.999999`  
**Actual portal return:** `6583.56144525802`  
**Progress:** new best `6583.561445` (previous `5709.3613`).  
**Strategy evidence:** Continue the validated boundary trajectory with a 0.10 x1 step. Marginal gain per unit x1 has been increasing, and independent local quadratic / GP checks both forecast roughly 6454..  
**Forecast recorded before outcome:** `6454.0`.  
**Lesson learnt (retrospective):** Another 0.10 x1 increase returned 6583.561.  
**Source:** [round 9 evidence](../../journey/round_09/README.md) · [related preserved code](../../journey/round_09/round9_controlled_fits.py) (*related historical analysis not verified exact*).

### Round 10

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Actual portal return:** `8662.405001248297`  
**Progress:** new best `8662.405001` (previous `6583.5614`).  
**Strategy evidence:** Upper-bound exploitation supported by nine observed gains and cubic challenger.  
**Lesson learnt (retrospective):** Testing the legal upper corner returned 8662.405; the full equation came later.  
**Source:** [round 10 evidence](../../journey/round_10/README.md) · [related preserved code](../../src/bbo/optimizer.py) (*related challenger not verified exact*).

### Round 11

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Actual portal return:** `8662.405001248297`  
**Progress:** no new best; incumbent `8662.40500` retained.  
**Strategy evidence:** Alternative-region exploration and structural investigations.  
**Lesson learnt (retrospective):** The repeated corner reproduced the best but did not test other regions.  
**Source:** [round 11 evidence](../../journey/round_11/README.md) · Exact original selection script not retained.

### Round 12

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Actual portal return:** `8662.405001248297`  
**Progress:** no new best; incumbent `8662.40500` retained.  
**Strategy evidence:** Controlled probes, repeats and structural investigations.  
**Lesson learnt (retrospective):** Another repeat confirmed the score at the same input only.  
**Source:** [round 12 evidence](../../journey/round_12/README.md) · Exact original selection script not retained.

### Round 13

**Submitted input:** `0.999999-0.999999-0.999999-0.999999`  
**Actual portal return:** `8662.405001248297`  
**Progress:** no new best; incumbent `8662.40500` retained.  
**Strategy evidence:** Final exploitation and regional probes.  
**Lesson learnt (retrospective):** The best legal input was retained; global optimality for the hidden code was not established.  
**Source:** [round 13 evidence](../../journey/round_13/README.md) · Exact original selection script not retained.

## Per-function evidence

- [All observations](observations.csv): 20 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Preserved prospective forecasts

Recorded pre-result forecasts are distinguished from reconstructed estimates. Blank entries in the CSV mean no such numerical forecast was retained.

| Round | Recorded forecast | Actual result | Status |
|---:|---:|---:|---|
| 9 | `6454.0` | `6583.56144525802` | recorded before return |

## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

[F5 structural validation](../../src/bbo/structural_validation.py) documents a later analytic reconstruction.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
