# Function 1: inputs, outputs and model evidence

**2 input dimensions · 10 starting observations · 13 submitted queries · best observed output `1.99999999967618`.**

F1 revealed a sharp, high-value region after several near-zero returns. Its original complete sequence of trained models has not been retained.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.02-0.98` | `0.0` | `7.710875115e-16` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.052001-0.865999` | `-1.9632454298284602e-233` | `7.710875115e-16` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.636406-0.206433` | `2.69213108614911e-65` | `7.710875115e-16` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.999999-0.999999` | `1.517648729565899e-192` | `7.710875115e-16` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.75-0.75` | `1.3319145509281447e-22` | `7.710875115e-16` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.732524-0.7389` | `3.2554751168755075e-17` | `7.710875115e-16` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.730874-0.7318` | `1.3142529628112004e-15` **↑** | `1.314252963e-15` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.735874-0.729467` | `4.1970039548686525e-16` | `1.314252963e-15` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.729874-0.7318` | `1.921280788064022e-15` **↑** | `1.921280788e-15` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.582552-0.558941` | `0.000007264001184177771` **↑** | `0.000007264001184` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.628540-0.628540` | `1.9999999996761817` **↑** | `2.000000000` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.628540-0.628540` | `1.9999999996761817` | `2.000000000` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.628540-0.628540` | `1.9999999996761817` | `2.000000000` | [Evidence](../../journey/round_13/README.md) |

## Week-by-week development: actual inputs, outputs, strategy, code and lessons

Follow the same function from Round 1 to Round 13. The **portal input and output** are observed evidence, while the **lesson learnt** is retrospective interpretation. Strategy descriptions reproduce the available decision ledger; they do not assert that every related script generated the exact submitted point. Later structural reconstructions are never passed off as pre-result models. Read the table above for a compact results history, or use the sections below for the decision narrative.

### Round 1

**Submitted input:** `0.02-0.98`  
**Actual portal return:** `0.0`  
**Progress:** no new best; incumbent `7.71087511e-16` retained.  
**Strategy evidence:** GP and acquisition baseline (retrospective).  
**Lesson learnt (retrospective):** Broad exploration returned no signal; the GP could not locate a narrow positive peak.  
**Source:** [round 1 evidence](../../journey/round_01/README.md) · Exact original selection script not retained.

### Round 2

**Submitted input:** `0.052001-0.865999`  
**Actual portal return:** `-1.9632454298284602e-233`  
**Progress:** no new best; incumbent `7.71087511e-16` retained.  
**Strategy evidence:** GP and UCB working package.  
**Lesson learnt (retrospective):** A second distant UCB query remained effectively zero; uncertainty alone was insufficient.  
**Source:** [round 2 evidence](../../journey/round_02/README.md) · [related preserved code](../../journey/round_02/week2_ucb_course_aligned.py) (*related historical script not verified exact*).

### Round 3

**Submitted input:** `0.636406-0.206433`  
**Actual portal return:** `2.69213108614911e-65`  
**Progress:** no new best; incumbent `7.71087511e-16` retained.  
**Strategy evidence:** Function-specific EI or wider search (retrospective).  
**Lesson learnt (retrospective):** A different region produced an extremely small value; basic smoothness assumptions were unhelpful.  
**Source:** [round 3 evidence](../../journey/round_03/README.md) · Exact original selection script not retained.

### Round 4

**Submitted input:** `0.999999-0.999999`  
**Actual portal return:** `1.517648729565899e-192`  
**Progress:** no new best; incumbent `7.71087511e-16` retained.  
**Strategy evidence:** GP, SVM and neural-network diagnostics.  
**Lesson learnt (retrospective):** The upper corner was also negligible; boundary queries are not universally successful.  
**Source:** [round 4 evidence](../../journey/round_04/README.md) · [related preserved code](../../journey/round_04/capstone_bbo_week4_module15.py) (*related historical analysis not verified exact*).

### Round 5

**Submitted input:** `0.75-0.75`  
**Actual portal return:** `1.3319145509281447e-22`  
**Progress:** no new best; incumbent `7.71087511e-16` retained.  
**Strategy evidence:** Controlled coordinate probes (retrospective).  
**Lesson learnt (retrospective):** A diagonal probe failed to beat the starting best; scale needed attention.  
**Source:** [round 5 evidence](../../journey/round_05/README.md) · Exact original selection script not retained.

### Round 6

**Submitted input:** `0.732524-0.7389`  
**Actual portal return:** `3.2554751168755075e-17`  
**Progress:** no new best; incumbent `7.71087511e-16` retained.  
**Strategy evidence:** GP, ridge and MLP comparison; controlled local fit.  
**Lesson learnt (retrospective):** A local probe improved magnitude without setting a new best; the active basin remained unclear.  
**Source:** [round 6 evidence](../../journey/round_06/README.md) · [related preserved code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) (*related notebook original fitter missing*).

### Round 7

**Submitted input:** `0.730874-0.7318`  
**Actual portal return:** `1.3142529628112004e-15`  
**Progress:** new best `1.314252963e-15` (previous `7.7108751e-16`).  
**Strategy evidence:** ARD and local forecast investigations (retrospective).  
**Lesson learnt (retrospective):** A tiny new best demonstrated signal, but not the important peak.  
**Source:** [round 7 evidence](../../journey/round_07/README.md) · Exact original selection script not retained.

### Round 8

**Submitted input:** `0.735874-0.729467`  
**Actual portal return:** `4.1970039548686525e-16`  
**Progress:** no new best; incumbent `1.31425296e-15` retained.  
**Strategy evidence:** Rank-GP local consensus around the new Week 7 best; stay inside the near-zero basin while testing a small x1-up/x2-down move..  
**Lesson learnt (retrospective):** A small step away from the incumbent reduced performance; local refinement was insufficient.  
**Source:** [round 8 evidence](../../journey/round_08/README.md) · [related preserved code](../../journey/round_08/capstone_bbo_module19_round8.py) (*related historical analysis not verified exact*).

### Round 9

**Submitted input:** `0.729874-0.7318`  
**Actual portal return:** `1.921280788064022e-15`  
**Progress:** new best `1.921280788e-15` (previous `1.3142530e-15`).  
**Strategy evidence:** One-coordinate probe: move x1 down by 0.001 from the Week 7 incumbent while holding x2 fixed. The updated rank-GP committee favours lower x1, but the output scale is too pathological for a trustworthy numeric forecast..  
**Lesson learnt (retrospective):** A controlled coordinate probe improved the tiny incumbent; a new representation was still needed.  
**Source:** [round 9 evidence](../../journey/round_09/README.md) · [related preserved code](../../journey/round_09/round9_controlled_fits.py) (*related historical analysis not verified exact*).

### Round 10

**Submitted input:** `0.582552-0.558941`  
**Actual portal return:** `0.000007264001184177771`  
**Progress:** new best `0.000007264001184` (previous `1.9212808e-15`).  
**Strategy evidence:** Targeted positive-response region; exploratory near-peer evidence; unobserved.  
**Lesson learnt (retrospective):** Peer-informed exploration located a measurable positive region for subsequent reconstruction.  
**Source:** [round 10 evidence](../../journey/round_10/README.md) · [related preserved code](../../src/bbo/optimizer.py) (*related challenger not verified exact*).

### Round 11

**Submitted input:** `0.628540-0.628540`  
**Actual portal return:** `1.9999999996761817`  
**Progress:** new best `2.000000000` (previous `0.0000072640012`).  
**Strategy evidence:** Alternative-region exploration and structural investigations.  
**Lesson learnt (retrospective):** The oscillatory structural hypothesis located an input returning almost 2.  
**Source:** [round 11 evidence](../../journey/round_11/README.md) · Exact original selection script not retained.

### Round 12

**Submitted input:** `0.628540-0.628540`  
**Actual portal return:** `1.9999999996761817`  
**Progress:** no new best; incumbent `2.00000000` retained.  
**Strategy evidence:** Controlled probes, repeats and structural investigations.  
**Lesson learnt (retrospective):** Repeating the measured peak reproduced its score but gave no new spatial information.  
**Source:** [round 12 evidence](../../journey/round_12/README.md) · Exact original selection script not retained.

### Round 13

**Submitted input:** `0.628540-0.628540`  
**Actual portal return:** `1.9999999996761817`  
**Progress:** no new best; incumbent `2.00000000` retained.  
**Strategy evidence:** Final exploitation and regional probes.  
**Lesson learnt (retrospective):** The known best was retained; no unsupported candidate was treated as an improvement.  
**Source:** [round 13 evidence](../../journey/round_13/README.md) · Exact original selection script not retained.

## Per-function evidence

- [All observations](observations.csv): 10 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

No fully authenticated source equation is claimed for this function.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
