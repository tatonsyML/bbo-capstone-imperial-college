# Round 13 | Three new records and the final portal return

**Status:** Confirmed eight portal outputs. This closes the thirteen-round challenge.

## What I did

I retained three high-scoring settings and used remaining queries to test new input regions for F2, F3, F4, F6 and a microscopic coordinate change for F7.

## What happened

| Function | Best after R12 | R13 observed | New record? |
|---|---:|---:|---|
| F1 | 1.9999999996761817 | 1.9999999996761817 | No, exact repeat |
| F2 | 0.6953368270741286 | **0.7442504263021256** | **Yes** |
| F3 | −0.005709220275560069 | **−0.0037530969187192596** | **Yes** |
| F4 | 0.7304594213260924 | **0.7468979113807426** | **Yes** |
| F5 | 8662.405001248297 | 8662.405001248297 | No, exact repeat |
| F6 | −0.03751864724436928 | −0.07698028695699928 | No |
| F7 | 3.3223680113931557 | 3.322368011392718 | No, differs by −4.38e−13 |
| F8 | 10 | 10 | No, exact repeat |

**Three new personal bests:** F2, F3 and F4. F1, F5 and F8 repeated exactly. F7 changed x1 from 0.201689 to 0.201690 and scored 4.38 × 10⁻¹³ lower, so it was not an identical query. F6 was below its Round 12 best.

## What I learnt

An apparent plateau is not evidence of global convergence. Changes in search region still produced useful improvements even in the final round.

## How I approached this round

Repeated millionth-size F4 moves produced tiny gains, while a later wider step helped. I described this in **_The trouble with the sixth decimal_**. I used forecast errors to refine the final-query strategy. I considered a **small distinct F8 step** near the optimum, but ultimately **submitted the same vertex** and received 10. The [recorded input](queries.txt) shows what I submitted, rather than every option considered.


## Original evidence

[Submitted inputs](queries.txt) · [returned outputs](outputs.txt) · [Week 13 portal CSV](../../data/portal_rounds_13.csv) · [verified bests](../../results/current_best_after_week13.csv).

## Detailed final-round analysis

## Final-round implications

**F2:** At `0.864900-0.500000`, the portal returned **0.7442504263021256**, a rise of **0.0489135992** (**7.03%**) over R12's best. Earlier local forecast failures and plateaus did not establish convergence across the domain.

**F3:** At `0.197280-0.523429-0.470094`, the portal returned **−0.0037530969187192596**, an improvement of **0.0019561234**. The exact underlying equation is still unresolved.

**F4:** At `0.416903-0.415704-0.360320-0.415205`, the portal returned **0.7468979113807426**, a gain of **0.0164384901** beyond the R11 result. This reinforces the importance of investigating productive regions beyond microscopic exploitation.

**F6:** R13 scored −0.076980, lower than the R12 incumbent −0.037519. **F7:** R13 shifted x1 from 0.201689 to 0.201690 and scored **3.322368011392718**, only **4.38 × 10⁻¹³** lower than R12, so it is not an exact repeat. **F1/F5/F8:** submitted repeated best inputs and returned identical scores.

## Evidence and limitations

Final dataset: **175 supplied initial observations + 104 personal returned queries (13 rounds × eight functions) = 279 observed records**, including repeated settings. Publicly reported peer observations do not count as personal returns. The confirmed Round 11 F7 input was `0.233000-0.128000-0.522000-0.276000-0.310000-0.667000`, returning `3.278967926227992`. It is confirmed in the [canonical observations](../../data/all_observations.csv) and [Round 11 record](../round_11/README.md). The original candidate-selection script is not available.

The result email contains observed scores, not prior model predictions. These post-result interpretations **do not establish prospective forecasts** or global optimality for unresolved functions.

[Round 13 inputs/outputs](../../data/portal_rounds_13.csv) · [Final best scores and inputs](../../results/current_best_after_week13.csv) · [Cumulative history](../../data/accumulated/history_through_week13.csv) · [Provenance](../../DATASHEET.md)

