# Input-space clustering | contemporary research, retrospective code

[← Methods and experiments](../../../methods/README.md) · [Round 11 evidence](../../../journey/round_11/README.md) · [F1 research](../../../functions/F1/README.md)

The author's **original Week 11 submission describes applying DBSCAN** to the 255 observations available through Round 10, including numerical cluster findings. **Clustering was therefore part of the contemporary Week 11 research.** The reproducible Python diagnostic in this folder was assembled and executed **later**, and its original relationship to the Week 11 implementation is not established. It was **not the verified original Round 11 candidate generator**. The [weekly-submission audit](../../../docs/WEEKLY_SUBMISSION_EVIDENCE.md) records this source distinction.

The analysis uses **only my 255 historical observations**: 175 course-supplied starting evaluations and 80 personal portal evaluations (10 rounds × 8 functions). No peer observations or additional oracle queries enter this clustering analysis. The source CSVs stay in their existing [`data/accumulated/function_N/` folders](../../../data/accumulated/), **not duplicated here**.

## What was tested

The reproducible [DBSCAN audit](clustering_audit.py) clusters **input coordinates only**, using Euclidean distance and `min_samples=3`. It tests seven values of `eps` (`0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.12`) for each of the eight functions, measuring the number of clusters and unclustered points. It also reports the highest **observed** score in each cluster and whether the best observed score through Round 10 is a DBSCAN noise point. The latter is not a prediction of score from clustering.

### Results at the original script's selected `eps`

| Function | Inputs | `eps` | Clusters | Unclustered | Best observed point unclustered? |
|---|---:|---:|---:|---:|---|
| F1 | 20 | 0.020 | 1 | 15 | **Yes** |
| F2 | 20 | 0.005 | 1 | 13 | No |
| F3 | 25 | 0.020 | 1 | 20 | Yes |
| F4 | 40 | 0.020 | 1 | 32 | No |
| F5 | 30 | 0.050 | 0 | 30 | Yes |
| F6 | 30 | 0.030 | 1 | 23 | Yes |
| F7 | 40 | 0.050 | 1 | 35 | Yes |
| F8 | 50 | 0.050 | 2 | 43 | Yes |

**Interpretation:** before Round 11, F1's best recorded value came from an isolated input rather than the five-point cluster near `(0.732, 0.733)`; the latter had extremely small scores. The F8 score of 10 was likewise outside both clusters. F2 and F4 had repeated investigation of productive local neighbourhoods. These are **descriptive observations** under the chosen density thresholds, not evidence that DBSCAN itself optimised the functions.

The full [sensitivity table](dbscan_eps_sensitivity.csv) shows that detected clusters depend on `eps`. Particularly in higher dimensions, fixed Euclidean neighbourhoods and a small sample size can label many points as noise without implying that those samples are unusual in the underlying objective. Changing `eps`, the distance metric or input scaling can change the result. The original data contain no exact duplicate input vectors at this cutoff, so the audit retains all 255 points and deliberately fails if new duplicates appear without an explicit policy.

## F1 diagnostic figure

![Full input-space clustering and reconstructed F1 overlay](f1_clustering_diagnostic.png)

The **left panel** shows only the 20 actual starting and portal inputs available through Round 10, including DBSCAN membership and the best recorded input. The **right panel** overlays those inputs on the **retrospectively reconstructed** two-peak F1 model from the canonical [F1 reconstruction](../../../src/bbo/f1_reconstruction.py). Model contours and fitted centres are not measured evaluations and **must not be interpreted as information available when Round 11 candidates were selected**. They simply help readers understand why input-space density did not coincide with high response.

## Reproduce

From the repository root, after `pip install -r requirements.txt`:

```bash
python research/diagnostics/clustering/clustering_audit.py --repo .
```

This writes three files beside the script:

- [`dbscan_eps_sensitivity.csv`](dbscan_eps_sensitivity.csv): 56 rows covering all seven radii and eight functions.
- [`selected_cluster_summary.csv`](selected_cluster_summary.csv): the 8 best observed points and 8 selected density clusters, with observed score summaries.
- [`f1_clustering_diagnostic.png`](f1_clustering_diagnostic.png): regenerated, clearly separated observed input and later model views.

This executable diagnostic is based on the later `bbo_clustering_audit.py` analysis. The **DBSCAN investigation was part of Week 11**, but this particular script is not verified as the original candidate-selection implementation. Its duplicate **F1/F8 equations, equation-validation CSVs and residual calculations were deliberately excluded**. This script uses the repository's existing F1 model only to draw the explanatory background; it does not re-fit F1 or reconstruct historical selection scripts.

[Original Round 11 evidence](../../../journey/round_11/README.md) · [Full observed dataset](../../../data/all_observations.csv) · [Evidence provenance](../../../docs/EVIDENCE_RULES.md).
