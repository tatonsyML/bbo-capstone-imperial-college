# Capstone BBO – Module 17 / Round 6

This package supports the sixth BBO query submission and the 17.1 reflection.

## Experiments
1. Five-fold comparison of Ridge, a small one-hidden-layer MLP and the current GP.
2. Controlled local path fits where previous rounds deliberately changed one direction.
3. Query selection that gives direct controlled evidence priority over a smoothed global surrogate.
4. A conservative local rank-GP choice for Function 1 because its raw outputs span extreme orders of magnitude.

## Why no CNN surrogate?
Module 17's CNN concepts are used as design principles, not forced onto the BBO coordinate vectors. The BBO inputs are tabular coordinates without the spatial translation structure that makes convolution and weight sharing appropriate for images.

## Files
- `capstone_bbo_module17_week6.py` – reproducible analysis.
- `results/model_comparison_round5.csv`
- `results/controlled_local_experiments.csv`
- `results/round6_queries.csv`
- `results/round6_portal_values.txt`
- `results/round6_query_rationale.csv`

The original package expected the programme seed data locally. Those seed arrays are deliberately not republished here.
