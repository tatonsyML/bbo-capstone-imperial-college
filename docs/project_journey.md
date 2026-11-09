# Project journey: from GP recommendations to evidence-gated decisions

This is the human-readable timeline. It links the decisions to preserved records without pretending every historical script is a complete reproduction.

| Round | Module | What changed | Evidence to inspect |
|---|---:|---|---|
| **R1** | 12 | Baseline review and first portal queries | [Round 1](../experiments/round_01/) |
| **R2** | 13 | UCB candidates, including wider searches | [Round 2](../experiments/round_02/) · [module package](../submissions/stage_2/modules/module_13_round_2/) |
| **R3** | 14 | EI and function-specific proposal policies | [Round 3](../experiments/round_03/) |
| **R4** | 15 | Hybrid GP/SVM/neural-network challenges | [Module 15 notebook](../submissions/stage_2/modules/module_15_round_4/) |
| **R5** | 16 | Controlled coordinate changes | [Round 5](../experiments/round_05/) |
| **R6** | 17 | Compare GP vs MLP; controlled local experiments | [Module 17](../submissions/stage_2/modules/module_17_round_6/) |
| **R7** | 18 | ARD kernels and sequential forecast checks | [Round 7](../experiments/round_07/) |
| **R8** | 19 | Wider experimental audits and local search | [Module 19](../submissions/stage_2/modules/module_19_round_8/) |
| **R9** | 20 | Forecast failures and stalled local gains | [Module 20](../submissions/stage_2/modules/module_20_round_9/) · [audit CSV](../results/week9_forecast_audit.csv) |
| **R10** | 21 | Model challengers, revised regions; F5/F8 records | [Round 10](../experiments/round_10/) · [revision audit](../results/round10_revision_audit.md) |
| **R11** | — | Structural F1; wider F4; F1–F4 new bests | [Round 11](../experiments/round_11/) |
| **R12** | — | Structural F7 forecast; F6/F7 new bests; four repeats | [Round 12](../experiments/round_12/) · [full evidence](round12_evidence.md) |
| **R13** | — | New bests for F2/F3/F4; all eight final outputs received | [Round 13 inputs and outputs](../experiments/round_13/) · [final evidence](round13_evidence.md) · [retrospective addendum](../submissions/stage_2/component_25_1/round13_addendum.md) |

## Three turning points

**Moving beyond the model's suggestion.** Controlled coordinate probes and forecast-versus-return checks showed that small predicted gains were not always achieved.

**Changing the search policy.** F4 improved sharply only after the search moved beyond excessively tiny local steps. F5 and F7 benefited from testing regions beyond earlier incumbents.

**Testing structure rather than endlessly tuning kernels.** F1, F5, F7 and F8 received numerical reconstructions with different levels of independent validation. F8 is particularly reproducible because the initial-40-only quadratic test and 13 later returns are present in this repository.

## What counts as a record?

The [experiments](../experiments/) folder preserves dated query and return files where available. [Stage 2 module submissions](../submissions/stage_2/modules/README.md) are historical course artefacts. [Current results](../results/current_best_after_week13.csv) and [provenance](evidence_provenance.md) describe what is verified now.

**Do not treat a dated forecast, proposed input or peer observation as an observed personal score.**

[Back to overview](../README.md) · [Function guide](function_guide.md) · [Reproduction](reproduce.md)
