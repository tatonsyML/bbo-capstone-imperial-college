# Function 6: inputs, outputs and model evidence

**5 input dimensions · 20 starting observations · 13 submitted queries · best observed output `-0.0375186472443693`.**

The five-dimensional F6 problem rewarded changes of search region and controlled diagnostics.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.440752-0.249118-0.839948-0.999999-1e-06` | `-0.6039806265819045` **↑** | `-0.6039806266` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.436716-0.004631-0.398416-0.895113-0.03487` | `-0.7529878928551597` | `-0.6039806266` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.467823-0.254239-0.82281-0.999999-0.03819` | `-0.5697790503980307` **↑** | `-0.5697790504` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.481359-0.2568-0.814241-0.999999-0.057285` | `-0.5414478319707962` **↑** | `-0.5414478320` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.494895-0.259361-0.805672-0.999999-0.07638` | `-0.5729927758567235` | `-0.5414478320` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.480996-0.256731-0.814471-0.999999-0.056773` | `-0.6980295508727566` | `-0.5414478320` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.48136-0.2568-0.814241-0.999999-0.057285` | `-0.5903792900833394` | `-0.5414478320` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.481358-0.2568-0.814241-0.999999-0.057285` | `-0.6337817154897656` | `-0.5414478320` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.481359-0.2568-0.814241-0.999999-0.057286` | `-0.5512864477685001` | `-0.5414478320` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.379322-0.338275-0.586412-0.727790-0.036539` | `-0.28565614419980845` **↑** | `-0.2856561442` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.457000-0.370000-0.642000-0.738000-0.020000` | `-0.12376148016289273` **↑** | `-0.1237614802` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.415080-0.344119-0.644062-0.776818-0.076258` | `-0.03751864724436928` **↑** | `-0.03751864724` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.420000-0.360000-0.650000-0.770000-0.100000` | `-0.07698028695699928` | `-0.03751864724` | [Evidence](../../journey/round_13/README.md) |

## Per-function evidence

- [All observations](observations.csv): 20 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

No fully authenticated source equation is claimed for this function.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
