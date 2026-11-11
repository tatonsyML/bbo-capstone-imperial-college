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

## Original weekly submission perspective

**Original Week 11 submission perspective:** My submitted reflection explicitly states **I applied DBSCAN** to the **255 own observations then available**, with Euclidean distance, **min_samples=3** and a neighbourhood-radius sensitivity sweep. For F1, **ε=0.02** gave one **five-point cluster** and **15 unclustered observations**; the best observed score was **outside** that cluster. This establishes the *contemporaneous clustering investigation*, not the exact provenance of the later repackaged Python audit. The Word submission also describes F1's two-component reconstruction and the measured F8 optimum.

*Source: the author's 52-page private `Capstone Project.docx` collection of weekly submissions, reviewed during the [13-week evidence reconciliation](../../docs/WEEKLY_SUBMISSION_EVIDENCE.md). The original document remains private. Its reflections support historical reasoning but do not replace portal returns or missing original scripts.*

## Contemporary clustering research and later executable diagnostic

**The original Week 11 submission explicitly discusses an applied DBSCAN investigation** of the **255 observations available through Round 10**, including Euclidean distance, radius sensitivity and observed cluster behaviour. This establishes a contemporaneous research account, although the exact original clustering script has not been authenticated.

The [published reproducible clustering diagnostic](../../research/diagnostics/clustering/README.md) was rebuilt **retrospectively** and is **not** the original candidate-selection implementation. Its [F1 figure](../../research/diagnostics/clustering/f1_clustering_diagnostic.png) separates actual prior inputs from a **later reconstructed model surface**. Neither the later code nor the smooth model overlay is presented as a prospective Round 11 forecast.

## Original evidence

[Returned values](outputs.txt) · [full portal CSV for R11–12](../../data/portal_rounds_11_12.csv) · [all observations](../../data/all_observations.csv). No contemporaneous complete Round 11 query text survived as a separate file; F7's vector was added later from verified course evidence.
