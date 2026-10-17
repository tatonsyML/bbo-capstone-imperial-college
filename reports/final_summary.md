# Current Project Summary — pre-Round 10

## Position

The project has evolved from a single-model Bayesian optimisation exercise into an evidence-gated sequential experimentation framework. The repository preserves observations, prospective forecasts, retrospective challengers and later interpretation separately.

## Current best observed values through Week 9

- F1: **1.92128078806402e-15** at `0.729874-0.731800`
- F2: **0.691314866323759** at `0.701500-0.959816`
- F3: **-0.0208561545295093** at `0.487816-0.639038-0.365586`
- F4: **0.658932867221058** at `0.420380-0.427768-0.368794-0.412497`
- F5: **6583.56144525802** at `0.858373-0.999999-0.999999-0.999999`
- F6: **-0.541447831970796** at `0.481359-0.256800-0.814241-0.999999-0.057285`
- F7: **1.78633819779689** at `0.228702-0.369270-0.256273-0.262985-0.391467-0.834089`
- F8: **9.9324430095864** at `0.128076-0.104109-0.074587-0.102502-0.970754-0.314560-0.238989-0.536764`

## Round 10

Round 10 is prospective. The strategic split is:

- **Exploit/refine:** F4, F5, F7, F8
- **Diagnose:** F2
- **Restart:** F1, F3, F6

The exact F1, F3 and F6 restart coordinates remain provisional pending rerun. The strongest structural finding is F8: an additive quadratic with 17 coefficients fits all 49 observed values to numerical precision and implies the candidate `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000` with predicted value 10. This remains a hypothesis until the portal returns the result.

## Remaining-round principle

Every query should have two possible ways to pay for itself: improve the incumbent, or resolve an uncertainty that changes the next decision.
