# Round 8 · Module 19 | Test forecasts rather than assume they are correct

**Evidence:** [Submitted inputs](queries.txt) and [returned outputs](outputs.txt) are real portal records. The forecasts below were recorded before receiving the corresponding return.

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

## Original weekly submission perspective

**Original Week 8 submission perspective:** I used the LLM as an **analytical assistant**, not as a stochastic numerical optimiser. Structured prompts separated evidence, hypotheses and validation. Python checked final vectors for dimension, legal bounds, six-decimal precision and duplicates. A tiny F2 x2 change exposed a fragile local region; final candidates were chosen using code and recorded results, **not raw generated text**.

*Source: the author's 52-page private `Capstone Project.docx` collection of weekly submissions, reviewed during the [13-week evidence reconciliation](../../docs/WEEKLY_SUBMISSION_EVIDENCE.md). The original document remains private. Its reflections support the historical reasoning but do not replace portal returns or missing original scripts.*

## Original files and provenance

Archived from the Module 19 ZIP dated **8 October 2026**, with programme-supplied NumPy seed files omitted. [Original analysis](capstone_bbo_module19_round8.py), [Round 8 query record](results/round8_queries.csv), [Week 7 audit](results/week7_audit.csv), [history through Week 7](results/submission_history_through_week7.csv) and [portal observations](../../data/all_observations.csv).
