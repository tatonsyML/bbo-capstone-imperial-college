# Round 11 | F1 breakthrough and stronger local search

**Results:** All eight submitted inputs and scores are confirmed by the portal records. F7's full input and score are documented in the official results email; its original candidate-generation script is unavailable.

## My reasoning at the time

After ten rounds I had 255 evaluated input-output pairs: 175 starting observations and 80 submitted queries. Week 10 had produced several personal bests, but no universal search pattern. F5 rose from about 6,583.56 to 8,662.41 near the legal boundary. F6 and F7 improved after relatively large movements from their previous incumbents. That contradicted the notion that refinement should always mean reducing step size. F2 still produced inconsistent scores for closely spaced inputs.

I applied DBSCAN to accumulated input coordinates using Euclidean distances on the common [0,1] scale, a minimum sample count of three, and a sweep of neighbourhood radius. The purpose was to understand where my search had concentrated, not to label the best part of the hidden surface. At a radius of 0.02, F1 had one small cluster but its strongest observed response lay outside it. F2 had a tight seven-point cluster at radius 0.005 containing materially different responses. F5 lacked a comparable cluster at radius 0.05, consistent with sparse, directional boundary probes. In F8, increasing the radius from 0.05 to 0.08 joined clusters, illustrating sensitivity to the choice of neighbourhood.

DBSCAN's noise label refers to low point density, not noisy objective measurements or poor function values. Because my inputs were selected adaptively, a cluster partly recorded where I had already decided to spend queries. It was dangerous to infer that the densest place was the best one. I wanted response-coloured plots, strong observations outside clusters and direct comparisons with later forecast accuracy.

F1 also led me to test structural and mathematical explanations. Outputs varying across many orders of magnitude made ordinary smooth GP interpolation difficult. A signed-log display offered a more useful view but did not prove a global equation. I distinguished numerical consistency on the available samples from genuine identification of the hidden function, and kept outside participants' observations separate from my own.

My next steps were to refine only where predictions had earned trust, challenge strong out-of-cluster observations and reassess models when observed errors exceeded plausible gains. I ended with three different maps in mind: where I had sampled, where the function performed well and where my predictions were reliable. They must not be confused.

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

A high-accuracy GP forecast is not enough if I confine the search to an unproductive neighbourhood. For F7, the input and full-precision result are confirmed by the official course email, not model-generated.

## How I approached this round

I applied **DBSCAN** to the **255 observations available through Round 10**, with Euclidean distance, **min_samples=3** and a neighbourhood-radius sensitivity sweep. For F1, **ε=0.02** gave one **five-point cluster** and **15 unclustered observations**; the best observed score was **outside** that cluster. This was part of my contemporary research. I also investigated F1's two-component response and the measured F8 optimum. The later published clustering script was reconstructed separately.


## Contemporary clustering research and later executable diagnostic

The **DBSCAN investigation examined 255 observations available through Round 10**, including Euclidean distance, radius sensitivity and observed cluster behaviour. The analysis was part of the Week 11 work, although the original executable clustering script has not been authenticated.

The [published reproducible clustering diagnostic](../../research/diagnostics/clustering/README.md) was rebuilt **retrospectively** and is **not** the original candidate-selection implementation. Its [F1 figure](../../research/diagnostics/clustering/f1_clustering_diagnostic.png) separates actual prior inputs from a **later reconstructed model surface**. Neither the later code nor the smooth model overlay is presented as a prospective Round 11 forecast.

## Original evidence

[Returned values](outputs.txt) · [full portal CSV for R11–12](../../data/portal_rounds_11_12.csv) · [all observations](../../data/all_observations.csv). No contemporaneous complete Round 11 query text survived as a separate file; F7's vector was added later from verified course evidence.
