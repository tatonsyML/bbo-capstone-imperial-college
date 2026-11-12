# Evidence and editorial principles

[← Project home](../README.md) · [Function stories](../functions/README.md)

This repository is organised **by function first**. The eight `functions/F1`–`F8` pages are the primary story; `journey/round_01`–`round_13` preserves the original chronology. Old snapshots belong under `archive/`, not in the homepage.

## The evidence hierarchy

1. **What was known at the time.** Dated decisions, historical code, forecasts and experimental notes describe each strategy and its uncertainty. The [research journey](WEEKLY_SUBMISSION_EVIDENCE.md) traces method changes across thirteen rounds. A proposed experiment is not an executed query; if the intended F8 adjustment differs from the actual R13 input, the official portal record prevails.
2. **What was actually submitted and returned.** Official course portal inputs and scores take priority. [F7 Round 11's input and score are confirmed](VERIFIED_FACTS.md); the original candidate-selection script is not available. The canonical [279-row dataset](../data/all_observations.csv) contains 175 supplied starting observations and 104 personal portal evaluations, including repeats. No peer observations are passed off as personal measurements.
3. **What was predicted beforehand.** Numeric forecasts appear as prospective evidence only if they are documented in a dated decision file, notebook or original notes. If no contemporary numerical forecast survives, its absence is recorded in the relevant decision ledger; the public account does not invent a value.
4. **What survived as code.** A historical script can be linked as *related surviving code* without claiming that it generated the exact submitted point. Missing seeds, kernel coefficients, restarts and transformations are not invented.
5. **What was learnt later.** Structural models, retrospective tests, full HEBO/TuRBO benchmark comparisons and interpretations of failures are described with their actual time and provenance.

## How the graphs work

**Measured progression** plots supplied and portal scores only. **Observed scatter** shows only recorded points. **Reconstructed surfaces** are always labelled as models with varying dimensions and fixed-coordinate settings stated. A modelled surface is never represented as extra black-box evaluations. Numerical validation evidence matters more than a visually smooth plot.

## Mathematical claims

- **F1:** A previously proposed two-component Gaussian–cosine family is now published with six explicit fitted coefficients. A **new retrospective fit uses only the author's 10 course-provided F1 observations**, and checks the 13 later personal portal returns as hold-out results. This does not establish blind discovery of the family or rewrite earlier, separately documented exploratory history. The source of the supplied model family has not been independently verified.
- **F2/F3/F4:** No validated closed-form underlying equation.
- **F5:** Power-sum reconstruction supports the boundary behaviour; reconstructed after the boundary query.
- **F6:** Competing local/GP hypotheses; no proven response equation.
- **F7:** Positive Hartmann-6 hypothesis, supported by a prediction recorded before R12.
- **F8:** Fitted 17-coefficient additive quadratic with a negative-definite Hessian and tested vertex of 10. Independent prediction of later portal returns is retrospective when fitted on only 40 starting samples.

No reconstructed model is labelled an authenticated copy of undisclosed source code. Samples cannot prove a global optimum for functions without a sufficiently validated global structure.

## Editing rules

Maintain thirteen expandable rounds per function and keep the sequence explicit: **known → predicted → submitted → observed → learnt**. A method description does not by itself establish which specific script generated a query. Update data once in the canonical CSV. Prefer links to historical scripts rather than copying them into 104 different directories. When a record conflicts with a retrospective reflection, describe the discrepancy, do not silently rewrite the original.
