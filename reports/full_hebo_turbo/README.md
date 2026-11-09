# Full HEBO / TuRBO-1 benchmark results

**Full-engine results are not yet confirmed here.**

A [manual benchmark workflow](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/full-optimisers.yml) is available for actual execution and downloadable evidence artifacts.

The [core GitHub Actions checks](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml) passed the standard unit tests, syntax checks and structural validation. This is separate from running the optional full HEBO and BoTorch engines.

The implementation and explanatory unit tests are in [benchmarks/full_optimisers](../../benchmarks/full_optimisers/). The optional complete HEBO and BoTorch/GPyTorch benchmark **has not been run and published**, so there are no simulated comparison scores to report. The presence of this directory must not be interpreted as a completed benchmark.

After independently running the two engines, `benchmark.py --mode compare` will create `f8_simulation_comparison.csv` from the recorded per-engine simulated evaluations. The one-step proposals for F1–F8 remain **unscored** unless the real portal has returned those exact candidate inputs, which this benchmark does not assume.

This is **post-capstone retrospective research**, not evidence that official HEBO or TuRBO generated the original 13 rounds.

[Methodology](../../docs/optimisation_algorithms.md) · [Execution instructions](../../benchmarks/full_optimisers/README.md) · [Historical model and portal results](../../docs/round13_evidence.md)
