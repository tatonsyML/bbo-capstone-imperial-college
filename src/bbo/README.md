# Source code guide

**Two distinct code paths are intentionally preserved.**

| Purpose | Entry point | Context |
|---|---|---|
| **Historical GP and query challengers** | [pipeline.py](pipeline.py) | Week 9 data snapshot; original optimisation methods |
| **HEBO-inspired committee and TuRBO-style local EI** | [optimizer.py](optimizer.py) | Educational adaptations, NOT the complete optimisers |
| **GP fitted models and response transforms** | [surrogates.py](surrogates.py) | ARD kernels, RBF/Matérn, Yeo–Johnson |
| **Acquisition functions** | [acquisition.py](acquisition.py) | EI, PI, UCB and their intended trade-offs |
| **Sobol and local search utilities** | [search.py](search.py) | Legal-domain candidate generation |
| **Loaders and historical F8 checks** | [diagnostics.py](diagnostics.py) | Week 9 evidence cut |
| **Full 104-query historical evidence audit** | [evidence_audit.py](evidence_audit.py) | Compare every submitted vector and output with all eight function ledgers; protect the recovered F7 R11 record |\n| **Retrospective F7 equation check** | [f7_reconstruction.py](f7_reconstruction.py) | Evaluate the documented positive Hartmann-6 hypothesis on 30 initial + 13 later scores |\n| **Reproducible F1 retrospective reconstruction** | [f1_reconstruction.py](f1_reconstruction.py) | Fit six coefficients from own 10 initial F1 rows; validate 13 portal returns without peer data |
| **Reproducible F8 reconstruction** | [structural_validation.py](structural_validation.py) | 40 initial + 13 later returned observations |
| **Post-capstone full HEBO / TuRBO-1 comparison** | [benchmark.py](../../research/full_optimisers/benchmark.py) | Official HEBO + BoTorch TuRBO-1, simulated F8 only |

**Read first:** [Algorithm design and code explanation](../../docs/methods.md) · [Benchmark instructions](../../research/full_optimisers/README.md).

Historical source files now include detailed function docstrings and comments explaining *why* a model, transformation, acquisition score or trust region was chosen, and where its mathematical assumptions can fail. No model-generated unobserved point is labelled as a portal result.
