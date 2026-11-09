# Project journey: from GP recommendations to evidence-gated decisions

This is the human-readable timeline. It links the decisions to preserved records without pretending every historical script is a complete reproduction.

| Round | Module | What changed | Evidence to inspect |
|---|---:|---|---|
| **R1** | 12 | Baseline review and first portal queries | [Round 1](../../journey/round_01/README.md) |
| **R2** | 13 | UCB candidates, including wider searches | [Round 2](../../journey/round_02/README.md) · [module package](../../journey/round_02/README.md) |
| **R3** | 14 | EI and function-specific proposal policies | [Round 3](../../journey/round_03/README.md) |
| **R4** | 15 | Hybrid GP/SVM/neural-network challenges | [Module 15 notebook](../../journey/round_04/README.md) |
| **R5** | 16 | Controlled coordinate changes | [Round 5](../../journey/round_05/README.md) |
| **R6** | 17 | Compare GP vs MLP; controlled local experiments | [Module 17](../../journey/round_06/README.md) |
| **R7** | 18 | ARD kernels and sequential forecast checks | [Round 7](../../journey/round_07/README.md) |
| **R8** | 19 | Wider experimental audits and local search | [Module 19](../../journey/round_08/README.md) |
| **R9** | 20 | Forecast failures and stalled local gains | [Module 20](../../journey/round_09/README.md) · [audit CSV](../../results/week9_forecast_audit.csv) |
| **R10** | 21 | Model challengers, revised regions; F5/F8 records | [Round 10](../../journey/round_10/README.md) · [revision audit](../../journey/round_10/README.md) |
| **R11** | — | Structural F1; wider F4; F1–F4 new bests | [Round 11](../../journey/round_11/README.md) |
| **R12** | — | Structural F7 forecast; F6/F7 new bests; four repeats | [Round 12](../../journey/round_12/README.md) · [full evidence](../../journey/round_12/README.md) |
| **R13** | — | New bests for F2/F3/F4; all eight final outputs received | [Round 13 inputs and outputs](../../journey/round_13/README.md) · [final evidence](../../journey/round_13/README.md) · [retrospective addendum](../../journey/final_reflection/round13_addendum.md) |

## Three turning points

**Moving beyond the model's suggestion.** Controlled coordinate probes and forecast-versus-return checks showed that small predicted gains were not always achieved.

**Changing the search policy.** F4 improved sharply only after the search moved beyond excessively tiny local steps. F5 and F7 benefited from testing regions beyond earlier incumbents.

**Testing structure rather than endlessly tuning kernels.** F1, F5, F7 and F8 received numerical reconstructions with different levels of independent validation. F8 is particularly reproducible because the initial-40-only quadratic test and 13 later returns are present in this repository.

## What counts as a record?

The [experiments](../../journey/README.md) folder preserves dated query and return files where available. [Stage 2 module submissions](../../journey/README.md) are historical course artefacts. [Current results](../../results/current_best_after_week13.csv) and [provenance](../../DATASHEET.md) describe what is verified now.

**Do not treat a dated forecast, proposed input or peer observation as an observed personal score.**

[Back to overview](../../README.md) · [Function guide](functions.md) · [Reproduction](methods.md)
