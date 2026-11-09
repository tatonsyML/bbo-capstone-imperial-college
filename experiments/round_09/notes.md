# Round 9 | forecasting accuracy versus search effectiveness

**Portal evidence:** [queries.txt](queries.txt) · [outputs.txt](outputs.txt). Predictions below were recorded before the returned outcomes and are independently listed in the [Week 9 forecast audit](../../reports/week9_forecast_audit.csv).

| Function | Forecast | Actual output | Interpretation |
|---|---:|---:|---|
| F2 | 0.730502 | 0.505526 | Large absolute error ≈ 0.224977; reduce trust in the local prediction |
| F3 | −0.020112 | −0.025816 | Small but meaningful miss |
| F4 | 0.658932869 | 0.658932867 | Accuracy ≈ 1.6 × 10⁻⁹, but the search region later proved too narrow |
| F5 | 6454 | 6583.561 | Improvement direction correct; gain underestimated |
| F7 | 1.786415 | 1.786338 | Small prediction error |
| F8 | 9.933511 | 9.932443 | Small prediction error |

There was no trustworthy scalar prediction for F1 or F6 in the preserved audit. These results explain why I later separated **model calibration** from **the quality of the region chosen for the next experiment**.

[Complete observations](../../data/all_observations.csv) · [Function explanations](../../docs/function_guide.md)
