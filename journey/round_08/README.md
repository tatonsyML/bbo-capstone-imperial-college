# Round 8 · Module 19 | Test forecasts rather than assume they are correct

**Evidence:** [Submitted inputs](queries.txt) and [returned outputs](outputs.txt) are real portal records. The forecasts below were recorded before receiving the corresponding return.

> **About this account:** Edited from my Week 8 entry in the 52-page *Capstone Project* reflection document. It preserves the reasoning available at the time; the confirmed portal results, historical source files and later provenance checks are retained below. Where an intention differs from a submitted input, the portal record is authoritative.

## My reasoning at the time

The LLM had become an analytical partner, but not my numerical optimiser. Early prompts were open-ended: I presented the observations and asked what they suggested. By this week I used a more disciplined pattern: verified observations, the previous query and its return, forecasts written before the return arrived, model diagnostics and competing candidates. I stopped asking one prompt to audit the data, choose a model, propose a point and judge its own work.

Deterministic Python code remained responsible for numerical fitting, candidate generation, duplicate detection and bounds checking. I used language-model assistance to compare explanations, identify assumptions and challenge conclusions. Externally shared observations were supporting evidence, not substitutes for my own portal returns. An attractive explanation was not accepted as a fact until the data supported it.

The eight functions required different questions. For F1 I considered rank-based GP ideas because most observed responses were nearly zero. F2 and F3 called for local brackets and interpolation checks. F5 and F7 supplied paths along which controlled trends were more informative than a large global search. On F8 I compared three GP kernels rather than assuming a single covariance function was correct. I kept F4 and F6 as controlled tests even where a trustworthy numerical forecast was unavailable.

I wanted each candidate to be falsifiable. Before submission, a record should identify the chosen point, the incumbent best, the predicted output where defensible, model disagreement and the specific claim the query would test. After receiving the portal score, I could compare the forecast with the return rather than quietly revising the explanation. This was the principal change in my use of AI: it widened the hypotheses I considered, while the numerical tools and returned observations determined which claims I believed.

## Verified results, methods and original evidence

## What I did

The retained [Round 8 Python analysis](capstone_bbo_module19_round8.py) tested rank-GP ideas for F1, local brackets for F2/F3, controlled trends for F5/F7 and GP-kernel agreement for F8. F4 and F6 were deliberately controlled experiments. A duplicate check protected the portal budget.

## What happened: preserved prospective forecasts

| Function | Prospective prediction recorded | Why it mattered |
|---|---:|---|
| F2 | Local quadratic ≈ 0.695189 at `0.701500-0.959720` | Test whether a narrow local model was reliable |
| F3 | Local-path ≈ −0.019675 | Check another near-incumbent direction |
| F5 | Local quadratic ≈ 5654.123 | Test whether the trend towards larger values persisted |
| F7 | Local quadratic ≈ 1.791396 | Challenge the existing regional model |
| F8 | Three GP-kernel predictions ≈ 9.902821, 9.906066, 9.907368 | Compare model agreement instead of trusting one kernel |

F1, F4 and F6 had **no reliable scalar forecast retained**; none has been invented.

## What I learnt

A local forecast needs direct portal validation. Controlled geometry can be more informative than a complicated global fit when the surface is poorly identified.

## How I approached this round

I used the LLM as an **analytical assistant**, not as a stochastic numerical optimiser. Structured prompts separated evidence, hypotheses and validation. Python checked final vectors for dimension, legal bounds, six-decimal precision and duplicates. A tiny F2 x2 change exposed a fragile local region; final candidates were chosen using code and recorded results, **not raw generated text**.


## Original files and provenance

Archived from the Module 19 ZIP dated **8 October 2026**, with programme-supplied NumPy seed files omitted. [Original analysis](capstone_bbo_module19_round8.py), [Round 8 query record](results/round8_queries.csv), [Week 7 audit](results/week7_audit.csv), [history through Week 7](results/submission_history_through_week7.csv) and [portal observations](../../data/all_observations.csv).
