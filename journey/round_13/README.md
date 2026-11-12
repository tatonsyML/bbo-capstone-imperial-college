# Round 13 | Three new records and the final portal return

**Final outcome:** Three new personal bests (F2, F3, F4), alongside five non-improving results. This closes the thirteen-round challenge.

## My reasoning at the time

One of my clearest lessons came from F4. Between Rounds 8 and 10, I changed a coordinate by as little as 0.000001. The score moved only from about 0.658930 to 0.658962. A later, wider step within the promising region returned 0.730459. A model might predict a tiny move with extraordinary accuracy while the underlying decision remained unproductive. Prediction error and decision value are separate questions.

My exploration strategy had changed with the budget. Early queries could be valuable because they improved knowledge used in several later rounds. Near the last evaluation, a new point needed a plausible chance of improving the incumbent immediately. F5 had shown the value of controlled single-coordinate changes, which eventually supported an upper-boundary score above 8,662. F2 demanded competing regions rather than endless trust in a narrow local fit. The Week 9 F2 prediction around 0.731, followed by a 0.506 return, had made me discount that model.

I considered reinforcement-learning ideas in the reflection as comparisons, not algorithms I had implemented. A Q-learning update uses observed reward and a discounted next-state value. My Gaussian Process instead updated predictions of immediate outputs and their related uncertainty. The procedure resembled one-step model-based experiment selection. A single portal score belonged to a selected query, so feedback could inform the next round but did not create an extended sequential reward path.

Round 12's four exact repeats provided repeatability evidence without discovering new nearby behaviour. F7 improved from about 3.278968 to 3.322368, consistent with a forecast recorded in advance, which strengthened the case for its local structural model. I became more sceptical of exact repeats without a specific measurement reason.

I considered a small neighbouring F8 query, but ultimately repeated the established optimum at (0.100000, 0.150000, 0.130000, 0.150000, 0.800000, 0.500000, 0.200000, 0.600000). The portal returned 10 again. Round 13 improved F2, F3 and F4, but not F6 or F7.

I also considered how the discipline might transfer to tuning an Oracle HCM data extract: testing batch size and concurrency, verifying full reconciliation, and rewarding genuine runtime improvements per experiment rather than a promising forecast alone. That was a proposed application, not a deployed solution. My closing lesson was to preserve the full chain from hypothesis to query to result, and to challenge decisions even when the surrogate appeared accurate.

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


## Inputs and results

[Submitted inputs](queries.txt) · [returned outputs](outputs.txt) · [Week 13 portal CSV](../../data/portal_rounds_13.csv) · [final best scores](../../results/current_best_after_week13.csv).

## Final-round implications

**F2:** At `0.864900-0.500000`, the portal returned **0.7442504263021256**, a rise of **0.0489135992** (**7.03%**) over R12's best. Earlier local forecast failures and plateaus did not establish convergence across the domain.

**F3:** At `0.197280-0.523429-0.470094`, the portal returned **−0.0037530969187192596**, an improvement of **0.0019561234**. The exact underlying equation is still unresolved.

**F4:** At `0.416903-0.415704-0.360320-0.415205`, the portal returned **0.7468979113807426**, a gain of **0.0164384901** beyond the R11 result. This reinforces the importance of investigating productive regions beyond microscopic exploitation.

**F6:** R13 scored −0.076980, lower than the R12 incumbent −0.037519. **F7:** R13 shifted x1 from 0.201689 to 0.201690 and scored **3.322368011392718**, only **4.38 × 10⁻¹³** lower than R12, so it is not an exact repeat. **F1/F5/F8:** submitted repeated best inputs and returned identical scores.

[Round 13 inputs/outputs](../../data/portal_rounds_13.csv) · [Final best scores and inputs](../../results/current_best_after_week13.csv) · [Cumulative history](../../data/accumulated/history_through_week13.csv) · [Final reflection](../final_reflection/README.md)
