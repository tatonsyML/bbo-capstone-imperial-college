# Evidence and editorial principles

[← Project home](../README.md) · [Function stories](../functions/README.md)

This repository is organised **by function first**. The eight `functions/F1`–`F8` pages are the primary story; `journey/round_01`–`round_13` preserves the original chronology. Old snapshots belong under `archive/`, not in the homepage.

## The evidence hierarchy

1. **What was known at the time.** The author's original 52-page *Capstone Project* weekly reflection document, plus preserved historical scripts and notes, describes intended methodology and uncertainty. Its content informs concise paraphrases, not fabricated exact forecasts. The complete private working document is not duplicated in the public repository.
2. **What was actually submitted and returned.** Official course portal inputs and scores take priority. The canonical [279-row dataset](../data/all_observations.csv) contains 175 supplied starting observations and 104 personal portal evaluations, including repeats. No peer observations are passed off as personal measurements.
3. **What was predicted beforehand.** Numeric forecasts appear as prospective evidence only if they are documented in a dated decision file, notebook or original notes. Otherwise, each weekly entry says the forecast was not retained.
4. **What survived as code.** A historical script can be linked as *related surviving code* without claiming that it generated the exact submitted point. Missing seeds, kernel coefficients, restarts and transformations are not invented.
5. **What was learnt later.** Structural models, retrospective tests, full HEBO/TuRBO benchmark comparisons and interpretations of failures are described with their actual time and provenance.

## How the graphs work

**Measured progression** plots supplied and portal scores only. **Observed scatter** shows only recorded points. **Reconstructed surfaces** are always labelled as models with varying dimensions and fixed-coordinate settings stated. A modelled surface is never represented as extra black-box evaluations. Numerical validation evidence matters more than a visually smooth plot.

## Mathematical claims

- **F1:** Empirically supported, externally informed oscillatory reconstruction. The complete coefficients are not retained publicly.
- **F2/F3/F4:** No validated closed-form underlying equation.
- **F5:** Power-sum reconstruction supports the boundary behaviour; recovered after the boundary query.
- **F6:** Competing local/GP hypotheses; no proven response equation.
- **F7:** Positive Hartmann-6 hypothesis, supported by a prediction recorded before R12.
- **F8:** Fitted 17-coefficient additive quadratic with a negative-definite Hessian and tested vertex of 10. Independent prediction of later portal returns is retrospective when fitted on only 40 starting samples.

No reconstructed model is labelled an authenticated copy of undisclosed source code. Samples cannot prove a global optimum for functions without a sufficiently validated global structure.

## Editing rules

Maintain thirteen expandable rounds per function and keep the sequence explicit: **known → predicted → submitted → observed → learnt**. Update data once in the canonical CSV. Prefer links to historical scripts rather than copying them into 104 different directories. When a record conflicts with a retrospective reflection, describe the discrepancy, do not silently rewrite the original.
