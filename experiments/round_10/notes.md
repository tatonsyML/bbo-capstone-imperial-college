# Round 10 | Portal submission and decision record

**Status:** Submitted and user-confirmed in the course portal. Scores are still pending.  
**Evidence cut:** 247 observed values through Week 9, plus eight unscored Round 10 queries.  
**Official submitted vectors:** [queries.txt](queries.txt)  
**Detailed evidence:** [Round 10 revision audit](../../reports/round10_revision_audit.md)

## Decisions and reasoning

- **F1** — 0.582552-0.558941. Targeted positive-response region; exploratory near-peer evidence; unobserved.
- **F2** — 0.701500-0.959796. Tight incumbent diagnostic after Week 9 GP forecast miss.
- **F3** — 0.469634-0.620072-0.416672. Alternative-region local interpolation; external evidence; uncertain.
- **F4** — 0.420370-0.427768-0.368794-0.412497. Controlled local refinement supported by prospective accuracy.
- **F5** — 0.999999-0.999999-0.999999-0.999999. Upper-bound exploitation supported by nine observed gains and cubic challenger.
- **F6** — 0.379322-0.338275-0.586412-0.727790-0.036539. Peer-informed GP regional exploration; model forecast only.
- **F7** — 0.190478-0.171014-0.347582-0.283057-0.283946-0.639922. Alternative basin; peer-informed ensemble; substantial uncertainty.
- **F8** — 0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000. 17-coefficient additive quadratic fitted vertex; predicted score 10.

## Superseded working proposals

The following points were **provisional alternatives**, not portal evaluations. They were replaced before the final Round 10 submission:

| Function | Earlier working candidate | Submitted Round 10 candidate |
|---|---|---|
| F1 | 0.472784-0.455748 | 0.582552-0.558941 |
| F3 | 0.325355-0.003391-0.538367 | 0.469634-0.620072-0.416672 |
| F6 | 0.437642-0.275181-0.565494-0.833184-0.042658 | 0.379322-0.338275-0.586412-0.727790-0.036539 |
| F7 | 0.223588-0.369270-0.256273-0.262985-0.391467-0.834089 | 0.190478-0.171014-0.347582-0.283057-0.283946-0.639922 |

F2, F4, F5 and F8 were retained unchanged. The external data used for some experimental reranking are not part of the 247 personally observed results. These choices do **not** acquire a true score until the portal response arrives.

## Evidence gate

HEBO-inspired, TuRBO-style and polynomial challengers offer competing hypotheses, not guaranteed scores. An evaluation is justified by plausible improvement or a useful reduction in uncertainty. Strong direct forecast validation outranks apparent model sophistication.
