# Full HEBO / TuRBO-1 benchmark results

**Full-engine results are not yet confirmed here.**

A [manual benchmark workflow](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/full-optimisers.yml) is available for actual execution and downloadable evidence artifacts.

The implementation and explanatory unit tests are in [benchmarks/full_optimisers](../../benchmarks/full_optimisers/). The current working runtime lacks both the official HEBO package and BoTorch/GPyTorch; therefore **there are no simulated comparison scores to publish here**. The presence of this directory must not be interpreted as a completed benchmark.

After independently running the two engines, \`benchmark.py --mode compare\` will create \`f8_simulation_comparison.csv\` from the recorded per-engine simulated evaluations. The one-step proposals for F1–F8 remain **unscored** unless the real portal has returned those exact candidate inputs, which this benchmark does not assume.

This is **post-capstone retrospective research**, not evidence that official HEBO or TuRBO generated the original 13 rounds.

[Methodology](../../docs/optimisation_algorithms.md) · [Execution instructions](../../benchmarks/full_optimisers/README.md) · [Historical model and portal results](../../docs/round13_evidence.md)
