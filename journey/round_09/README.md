# Round 9 · Module 20 | A correct forecast can still lead to poor search

**Evidence:** [Submitted inputs](queries.txt) and [returned outputs](outputs.txt) are the observed portal record. The forecasts below were recorded before the result, as documented in the [Week 9 audit](../../results/week9_forecast_audit.csv).

## My reasoning at the time

I began to consider the marginal value of another query. The portal evaluation budget was limited; offline fitting cost less, but adding models could also consume time and create confidence without improving a decision. I used scaling as an analogy for marginal return, not as a claim that a small Gaussian Process obeyed the scaling laws of a large language model.

The eight objectives showed sharply different progress. F4 had entered a region where tiny coordinate changes led to tiny score movements near 0.659. F5 still rewarded an observed direction towards the boundary. F8 offered more positive evidence: several GP kernels supported an input change and a later return improved from about 9.899002 to 9.911399. A common acquisition policy would conceal those differences.

I separated unexpected behaviour from the technical meaning of emergence in language models. F5's accelerating ridge was surprising, but was not proof of a new cognitive capability. A genuinely useful improvement in my analytical process would be the ability to recognise forecast failures, disagreeing diagnostics and decisions whose potential improvement was smaller than typical prediction error.

This round sharpened the distinction between numerical accuracy and query value. F2 demonstrated how a confident local forecast might fail badly. On F4, a highly accurate local model might still suggest a step too small to produce useful progress. F8 provided an example where agreement across alternative kernels supported an actionable choice. Robustness sometimes meant doing less: record a forecast before the return, change one coordinate when this gives an informative experiment, and stop adding complexity when it does not change the decision.

My remaining-budget principle was that a query should either improve the objective or reduce a specific uncertainty that would influence a later choice. Near the final evaluation, information with no further chance of application had less value. I no longer regarded exploitation, exploration or extra modelling effort as automatically desirable; each had to justify its cost.

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

## How I approached this round

I considered the *value of one more expensive query*, using **Week 8 forecast errors** as evidence. F2 had been forecast near **0.69519** and returned **0.61309**; F3 had been forecast near **−0.01968** and returned **−0.02966**. These observations belong to the preceding round and must not be confused with the **separate Round 9 F2 forecast** of ~**0.730502**, which later returned ~**0.505526**.


## Files

[Queries](queries.txt) · [Returns](outputs.txt) · [Week 8 audit](results/week8_audit.csv) · [scaling ledger](results/scaling_ledger.csv) · [cumulative historical records](results/submission_history_through_week8.csv).
