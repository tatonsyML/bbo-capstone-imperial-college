# Round 9 · Module 20 | A correct forecast can still lead to poor search

**Evidence:** [Submitted inputs](queries.txt) and [returned outputs](outputs.txt) are the observed portal record. The forecasts below were recorded before the result, as documented in the [Week 9 audit](../../results/week9_forecast_audit.csv).

## What I did

The [controlled fitting script](round9_controlled_fits.py) evaluated local polynomials for F2, F3, F4, F5 and F7, while [round9_queries.csv](results/round9_queries.csv) preserved the planned points and rationale. The package was archived on **14 October 2026**, before the Round 9 portal results were known. Programme seed arrays are not republished.

## What happened

| Function | Forecast | Actual output | Interpretation |
|---|---:|---:|---|
| F2 | 0.730502 | 0.505526 | Large absolute error ≈ 0.224977; reduce trust in the local prediction |
| F3 | −0.020112 | −0.025816 | Small but meaningful miss |
| F4 | 0.658932869 | 0.658932867 | Accuracy ≈ 1.6 × 10⁻⁹, but the search region later proved too narrow |
| F5 | 6454 | 6583.561 | Improvement direction correct; gain underestimated |
| F7 | 1.786415 | 1.786338 | Small prediction error |
| F8 | 9.933511 | 9.932443 | Small prediction error |

No reliable scalar forecast for F1 or F6 was retained.

## What I learnt

F4's exceptionally accurate local result did not identify a better search region, while F2's large miss undermined confidence in a narrow forecast. I began separating **prediction calibration** from **candidate selection quality**.

## Original weekly submission perspective

**Original Week 9 submission perspective:** I considered the *value of one more expensive query*, using **Week 8 forecast errors** as evidence. F2 had been forecast near **0.69519** and returned **0.61309**; F3 had been forecast near **−0.01968** and returned **−0.02966**. These observations belong to the preceding round and must not be confused with the **separate Round 9 F2 forecast** of ~**0.730502**, which later returned ~**0.505526**.

*Source: the author's 52-page private `Capstone Project.docx` collection of weekly submissions, reviewed during the [13-week evidence reconciliation](../../docs/WEEKLY_SUBMISSION_EVIDENCE.md). The original document remains private. Its reflections support the historical reasoning but do not replace portal returns or missing original scripts.*

## Files

[Queries](queries.txt) · [Returns](outputs.txt) · [Week 8 audit](results/week8_audit.csv) · [scaling ledger](results/scaling_ledger.csv) · [cumulative historical records](results/submission_history_through_week8.csv).
