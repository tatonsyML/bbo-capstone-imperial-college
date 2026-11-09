# Verified Round 13 evidence

The course Week 13 processing email confirms **eight input vectors and eight returned scores**, completing the challenge. This supplements the earlier [Round 12 snapshot](round12_evidence.md), not rewriting it.

| Function | Best through R12 | R13 result | Final best | First achieved |
|---|---:|---:|---:|---|
| F1 | 1.9999999996761817 | 1.9999999996761817 | 1.9999999996761817 | R11 |
| F2 | 0.6953368270741286 | **0.7442504263021256** | **0.7442504263021256** | **R13** |
| F3 | −0.005709220275560069 | **−0.0037530969187192596** | **−0.0037530969187192596** | **R13** |
| F4 | 0.7304594213260924 | **0.7468979113807426** | **0.7468979113807426** | **R13** |
| F5 | 8662.405001248297 | 8662.405001248297 | 8662.405001248297 | R10 |
| F6 | −0.03751864724436928 | −0.07698028695699928 | −0.03751864724436928 | R12 |
| F7 | 3.3223680113931557 | 3.322368011392718 | 3.3223680113931557 | R12 |
| F8 | 10 | 10 | 10 | R10 |

## Final-round implications

**F2:** At `0.864900-0.500000`, the portal returned **0.7442504263021256**, a rise of **0.0489135992** (**7.03%**) over R12's best. Earlier local forecast failures and plateaus did not establish convergence across the domain.

**F3:** At `0.197280-0.523429-0.470094`, the portal returned **−0.0037530969187192596**, an improvement of **0.0019561234**. The exact underlying equation is still unresolved.

**F4:** At `0.416903-0.415704-0.360320-0.415205`, the portal returned **0.7468979113807426**, a gain of **0.0164384901** beyond the R11 result. This reinforces the importance of investigating productive regions beyond microscopic exploitation.

**F6:** R13 scored −0.076980, lower than the R12 incumbent −0.037519. **F7:** R13 shifted x1 from 0.201689 to 0.201690 and scored **3.322368011392718**, only **4.38 × 10⁻¹³** lower than R12, so it is not an exact repeat. **F1/F5/F8:** submitted repeated best inputs and returned identical scores.

## Evidence and limitations

Final dataset: **175 supplied initial observations + 104 personal returned queries (13 rounds × eight functions) = 279 observed records**, including repeated settings. Publicly reported peer observations do not count as personal returns. The R11 F7 input is missing from the preserved evidence, though its returned score is documented.

The result email contains observed scores, not prior model predictions. These post-result interpretations **do not establish prospective forecasts** or global optimality for unresolved functions.

[Round 13 inputs/outputs](../data/portal_rounds_13.csv) · [Final best scores and inputs](../results/current_best_after_week13.csv) · [Cumulative history](../data/accumulated/history_through_week13.csv) · [Provenance](evidence_provenance.md)
