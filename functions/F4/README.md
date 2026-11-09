# Function 4: inputs, outputs and model evidence

**4 input dimensions · 30 starting observations · 13 submitted queries · best observed output `0.746897911380743`.**

Exceptionally accurate local forecasts still left F4 in a suboptimal search region.

## Every weekly portal submission

Each output is **measured**, not a GP prediction. **↑** marks a new best relative to all earlier real observations, including the course starting data. The third column shows the actual Round score; the fourth shows best-so-far, which is different.

| Round | Actual submitted coordinates | Actual portal output | Best so far | Historical rationale and available code |
|---:|---|---:|---:|---|
| [1](../../journey/round_01/README.md) | `0.5315-0.448817-0.362651-0.331977` | `-1.910544236949021` **↑** | `-1.910544237` | [Evidence](../../journey/round_01/README.md) |
| [2](../../journey/round_02/README.md) | `0.415636-0.429159-0.368928-0.413098` | `0.6475542651940924` **↑** | `0.6475542652` | [Evidence](../../journey/round_02/README.md) · [code](../../journey/round_02/week2_ucb_course_aligned.py) |
| [3](../../journey/round_03/README.md) | `0.398136-0.414095-0.370552-0.440336` | `0.3148998621282755` | `0.6475542652` | [Evidence](../../journey/round_03/README.md) |
| [4](../../journey/round_04/README.md) | `0.425128-0.426376-0.368659-0.411895` | `0.646639136105915` | `0.6475542652` | [Evidence](../../journey/round_04/README.md) · [code](../../journey/round_04/capstone_bbo_week4_module15.py) |
| [5](../../journey/round_05/README.md) | `0.420382-0.427768-0.368794-0.412497` | `0.6589269585907762` **↑** | `0.6589269586` | [Evidence](../../journey/round_05/README.md) |
| [6](../../journey/round_06/README.md) | `0.42029-0.427795-0.368797-0.412509` | `0.6589225038891553` | `0.6589269586` | [Evidence](../../journey/round_06/README.md) · [code](../../journey/round_06/Capstone_BBO_Module17_Week6.ipynb) |
| [7](../../journey/round_07/README.md) | `0.420383-0.427768-0.368794-0.412497` | `0.6589240028704428` | `0.6589269586` | [Evidence](../../journey/round_07/README.md) |
| [8](../../journey/round_08/README.md) | `0.420381-0.427768-0.368794-0.412497` | `0.6589299133743123` **↑** | `0.6589299134` | [Evidence](../../journey/round_08/results/round8_queries.csv) · [code](../../journey/round_08/capstone_bbo_module19_round8.py) |
| [9](../../journey/round_09/README.md) | `0.42038-0.427768-0.368794-0.412497` | `0.6589328672210581` **↑** | `0.6589328672` | [Evidence](../../journey/round_09/results/round9_queries.csv) · [code](../../journey/round_09/round9_controlled_fits.py) |
| [10](../../journey/round_10/README.md) | `0.420370-0.427768-0.368794-0.412497` | `0.6589623541690739` **↑** | `0.6589623542` | [Evidence](../../journey/round_10/round10_candidates.csv) · [code](../../src/bbo/optimizer.py) |
| [11](../../journey/round_11/README.md) | `0.415000-0.417000-0.366500-0.413000` | `0.7304594213260924` **↑** | `0.7304594213` | [Evidence](../../journey/round_11/README.md) |
| [12](../../journey/round_12/README.md) | `0.415000-0.417000-0.366500-0.413000` | `0.7304594213260924` | `0.7304594213` | [Evidence](../../journey/round_12/README.md) |
| [13](../../journey/round_13/README.md) | `0.416903-0.415704-0.360320-0.415205` | `0.7468979113807426` **↑** | `0.7468979114` | [Evidence](../../journey/round_13/README.md) |

## Per-function evidence

- [All observations](observations.csv): 30 initial records plus 13 submitted and returned scores, preserved at source precision.
- [Decision and provenance ledger](selection_history.csv): the 13 actual inputs, outcomes, pre-round data counts, rationales, related scripts, code-evidence status and available forecasts.
- [Replay and fitted-model guidance](model_runs/README.md): how to refit a **new** GP using only observations from before the chosen Round, and inspect learned kernel lengthscales.


## Preserved prospective forecasts

Recorded pre-result forecasts are distinguished from reconstructed estimates. Blank entries in the CSV mean no such numerical forecast was retained.

| Round | Recorded forecast | Actual result | Status |
|---:|---:|---:|---|
| 9 | `0.6589328687823797` | `0.6589328672210581` | recorded before return |

## Method and code provenance

Historical code references are linked in the round table where retained. A script related to a round is **not proof that those exact model settings generated every submitted input**. Exact saved GP model objects and per-round fitted lengthscales have not been retained for all 104 decisions.

No fully authenticated source equation is claimed for this function.

Our [shared GP code](../../src/bbo/surrogates.py), [acquisition functions](../../src/bbo/acquisition.py) and [candidate-generation utilities](../../src/bbo/search.py) apply to all eight functions with **separate fitted models**. [HEBO-inspired and TuRBO-style challengers](../../src/bbo/optimizer.py) differ from the [later official HEBO / BoTorch TuRBO-1 benchmark](../../research/full_optimisers/README.md); neither full reference engine is claimed as the historical submitter.

[All functions](../README.md) · [Chronological journey](../../journey/README.md) · [Final model card](../../MODEL_CARD.md).
