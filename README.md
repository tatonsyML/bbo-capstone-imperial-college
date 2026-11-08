# Black-Box Optimisation Capstone

Imperial College London | Professional Certificate in Machine Learning and Artificial Intelligence

**Latest verified evidence: Round 12.** The project contains 175 course-provided starting observations and 96 returned personal queries (12 rounds × eight functions), totalling **271 evaluations**, including repeated input locations. No Round 13 returns are represented as observed.

## Start here

1. **[Final Stage 2 retrospective](submissions/stage_2/component_25_1/retrospective.md)** — the full story and five assessment criteria.
2. [Evidence and results](docs/round12_evidence.md) — exact outcomes, the late-stage turnaround and the F2/F4/F8 diagnostic cases.
3. [Mathematical reconstruction](docs/structural_reconstruction.md) — the four supported function families, limitations and reproducible F8 test.
4. [Data provenance](docs/evidence_provenance.md) — personal evaluations versus course and publicly shared external records.
5. [Model card](docs/model_card.md) · [Datasheet](docs/datasheet.md) · [Decision log](docs/decision_log.md) · [Project journey](docs/project_journey.md).

## Confirmed results

| Function | Initial best | Best after R9 | Best through R12 | First achieved |
|---|---:|---:|---:|---:|
| F1 | 7.71e-16 | 1.92e-15 | **1.999999999676** | R11 |
| F2 | 0.611205 | 0.691315 | **0.695337** | R11 |
| F3 | -0.034835 | -0.020856 | **-0.005709** | R11 |
| F4 | -4.025542 | 0.658933 | **0.730459** | R11 |
| F5 | 1,088.860 | 6,583.561 | **8,662.405** | R10 |
| F6 | -0.714265 | -0.541448 | **-0.037519** | R12 |
| F7 | 1.364968 | 1.786338 | **3.322368** | R12 |
| F8 | 9.598482 | 9.932443 | **10.000000** | R10 |

All eight final confirmed bests were established in R10–R12. These are *best-so-far portal returns*, not scores from a single round. Function scores use different scales and must not be summed.

[Machine-readable bests](reports/current_best_after_week12.csv) · [Actual Round 11–12 returns](data/portal_rounds_11_12.csv)

## Three lessons from the experiments

- **Prediction reliability (F2):** pre-outcome forecast 0.730502, observed 0.505526. The error was approximately 0.225.
- **Search quality (F4):** a local forecast was accurate to about 1.6e-9, but tiny local steps held the search near 0.659. A larger movement scored 0.730459.
- **Mathematical suitability (F8):** an additive 17-coefficient quadratic explains the observed response and identifies the optimum of 10. A later initial-40-only retrospective fit predicts 12 subsequent returns to floating-point precision.

A good prediction, a good query and a suitable model representation are different achievements.

## Reproduce the strongest mathematical claim

The repository includes [52 F8 observations](data/accumulated/function_8/observations_through_week12.csv): **40 initial** and **12 later personal** evaluations, with repeats retained. The script below fits the quadratic *only on the 40 starting observations*, then predicts the later 12. It also checks the F5 boundary score.

~~~bash
python -m pip install -r requirements.txt
PYTHONPATH=src python -m bbo.structural_validation
PYTHONPATH=src python -m pytest -q
~~~

The original optimisation demo remains available via PYTHONPATH=src python -m bbo.pipeline, but its previously published data cut ends at Week 10. It is not a reproduction of every later retrospective experiment.

## Evidence and limitations

The leaderboard provided comparisons of attained outputs. A smaller number of public input-output records also helped redirect later candidates and validate some structural models. These were not counted as personal evaluations; their categories and methodological limits are documented in the [anonymised Round 10 audit](reports/round10_revision_audit.md); identifying source references should be retained separately for any required academic attribution. The official complete HEBO and TuRBO implementations were not benchmarked: the project evaluated selected inspired mechanisms.

The source audit confirms Round 11 F7's *output* but does not preserve its exact input coordinates. The [Round 11–12 CSV](data/portal_rounds_11_12.csv) leaves this coordinate empty rather than fabricating one. An earlier proposed Round 12 shortlist differs from the actual submitted F2, F3 and F6 queries; only observed portal returns are used in the results.

Historical files including the [model card](docs/model_card.md), [datasheet](docs/datasheet.md) and [older modules](submissions/stage_2/modules/) preserve their original dated evidence cuts. A statement such as “Round 10 pending” in an archived document is not the current repository status.
