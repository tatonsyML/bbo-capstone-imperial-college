# Round 11 | F1 breakthrough and stronger local search

**Status:** Observed portal results, not predictions. F7's input and full-precision score were later recovered from the official results email, rather than inferred from its score. The original selection code remains unavailable.

## What I did

I challenged the nearly flat F1 response near the earlier incumbent and explored alternative regions for F2/F3/F4. F1 reached a strong response and F4's wider move improved materially over its narrow local forecast region.

## What happened

| Function | Actual input | Returned score |
|---|---|---:|
| F1 | 0.628540-0.628540 | 1.9999999996761817 |
| F2 | 0.692000-0.366000 | 0.6953368270741286 |
| F3 | 0.445500-0.593000-0.420000 | -0.005709220275560069 |
| F4 | 0.415000-0.417000-0.366500-0.413000 | 0.7304594213260924 |
| F5 | 0.999999-0.999999-0.999999-0.999999 | 8662.405001248297 |
| F6 | 0.457000-0.370000-0.642000-0.738000-0.020000 | -0.12376148016289273 |
| F7 | 0.233000-0.128000-0.522000-0.276000-0.310000-0.667000 | 3.278967926227992 |
| F8 | 0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000 | 10 |

**New bests:** F1, F2, F3 and F4. F5 and F8 repeated earlier successes.

## What I learnt

A high-accuracy GP forecast is not enough if I confine the search to an unproductive neighbourhood. For F7, the input and full-precision result are recovered from the official course email, not model-generated.

## Supplementary recovered Python analysis

The [October clustering audit](supplementary_analysis/bbo_clustering_audit.py) evaluates DBSCAN neighbourhoods and numerical F1/F8 reconstruction against observations available through Round 10. It was transcribed from a separately retained Python file whose raw export was unavailable. It is **not confirmed as the exact source that selected Round 11 portal queries**. [See source-code availability by round](../CODE_AVAILABILITY.md).

## Original evidence

[Returned values](outputs.txt) · [full portal CSV for R11–12](../../data/portal_rounds_11_12.csv) · [all observations](../../data/all_observations.csv). No contemporaneous complete Round 11 query-selection file survived. [Verified inputs reconstructed from the portal records](queries_verified_from_portal.txt) provide all eight submitted vectors; this is not the original candidate-selection script.
