# Final Datasheet | BBO capstone observations

**Evidence through:** Round 13, 9 November 2026 · **Status:** Final documentation of the verified record

[← Project home](README.md) · [Complete data CSV](data/all_observations.csv) · [Final model card](MODEL_CARD.md)

## 1. Motivation and purpose

This dataset supports a sequential black-box optimisation exercise: select one input vector for each of eight hidden functions per round, observe a numeric score, and maximise the best observed output with few evaluations. The initial samples were supplied by the programme; the 13 later rounds of personal portal returns were submitted by the project author.

It is a historical record of *observed evaluations*, not a dataset of the true functions over their full domains.

## 2. Composition and fields

**279 recorded rows:** 175 course-provided initial observations and **104 personal portal evaluations** (13 rounds × 8 functions). The input dimensions are 2, 2, 3, 4, 4, 5, 6 and 8 for F1–F8 respectively.

| Field | Meaning |
|---|---|
| `function` | Function identifier, 1–8 |
| `round` | 0 for the supplied initial observations; 1–13 for personal queries |
| `stage` | Original source label, such as `Initial` or `Week 13` |
| `source`, `is_initial` | Distinguish course data from personally submitted queries |
| `sequence_in_stage` | Original ordering within the source stage |
| `input_status` | `confirmed` for all currently recorded inputs; `missing_input` was a transitional provenance status before confirmation |
| `x1`–`x8` | Input coordinates. Unused coordinates are blank for functions with fewer dimensions |
| `output` | Returned scalar score, preserving source precision where available |

**Previously incomplete input record ([canonical verified facts](docs/VERIFIED_FACTS.md)):** An official Round 11 results email confirmed F7's submitted input (`0.233000-0.128000-0.522000-0.276000-0.310000-0.667000`) and precise return (`3.278967926227992`). Earlier drafts contained the output without its coordinates; this gap was fixed from the original email, not inferred from a model. All **279 observed scores now have complete input vectors** within their respective function dimensions.

No synthetic labels, missing coordinates or unobserved outcomes are filled in.

## 3. Collection process and timing

The programme supplied 175 initial input/output pairs, then the author submitted one new query for each function in each of 13 rounds. The portal returned eight responses per round. The consolidated CSV combines the [per-function history through R10](data/accumulated/), [R11–12 returns](data/portal_rounds_11_12.csv) and [R13 returns](data/portal_rounds_13.csv). Duplicate query locations are retained because they represent actual evaluations.

The repository itself was assembled retrospectively from the preserved records. Its Git commit dates are **not** a contemporaneous timestamp for the original R1–R9 experiments.

## 4. Preparation and transformations

The CSV is a tidy union of already recorded numeric outputs, with provenance columns and unused dimensions left empty. It does **not** normalise response values, replace missing inputs or deduplicate repeated portal queries.

The working GP pipeline optionally applies Yeo–Johnson or signed-log transformations, and some visualisations use log-labelled scales. Those are *analysis and display choices*, not changes to the original `output` column.

## 5. Performance and results

The project records **279 outputs** in total: 175 starting observations and 104 personal portal returns. The final observed maxima are summarised below. Different functions have different scales; these values are not combined into one score.

| Function | Final personal best | First reached |
|---|---:|---|
| F1 | 1.9999999996761817 | R11 |
| F2 | 0.7442504263021256 | R13 |
| F3 | −0.0037530969187192596 | R13 |
| F4 | 0.7468979113807426 | R13 |
| F5 | 8662.405001248297 | R10 |
| F6 | −0.03751864724436928 | R12 |
| F7 | 3.3223680113931557 | R12 |
| F8 | 10 | R10 |

## 6. Weekly iteration and learning

One personally submitted evaluation per function was returned in each of **13 rounds**. The [round archive](journey/README.md) records actual inputs and outputs; the [project journey](archive/notes/early_project_timeline.md) explains how the search policy changed. Early rounds used GP and UCB/EI suggestions, later rounds included controlled probes and structural hypotheses, and the final round improved F2, F3 and F4. Retrospective explanations are labelled rather than passed off as pre-submission predictions.

## 7. Biases, limitations and appropriate use

Initial samples are sparse in high dimensions; later queries were selected adaptively and favour regions already thought promising. The result is **not a uniform representative sample** of each function. F1 contains extremely small outputs, F5 has a large response scale, and some series cluster strongly near incumbents. Cross-function raw scores cannot sensibly be averaged.

**Appropriate:** learning GP optimisation, auditing query selection, reproducing historical bests, testing simple surrogate hypotheses and evaluating held-out prediction.

**Inappropriate:** claiming a global optimum for unresolved functions, fitting the F8 model to all 53 points and calling the later 13 independent validation, or attributing peers' results to this participant. Chronological model-selection tests must avoid future-information leakage.

## 8. Distribution, permissions and privacy

The original course-provided `.npy` files are **not hosted here**. However, the **175 course-provided numerical observations do appear in public CSV files**. Permission to redistribute these numeric values has **not been independently verified**. The author should check the course's terms and, if necessary, restrict publication or replace the course rows with an authorised retrieval link. Do not infer an open data licence from this repository.

The dataset contains no reported personal identifiers or health records. The 175 supplied starting observations and 104 personally returned queries have separate source flags. External observations used as research evidence are **not** included among these 279 rows. [Data-use and redistribution statement](USAGE_AND_PERMISSIONS.md).

### Evidence provenance and historical context

- **Prospective evidence** means a query or forecast recorded *before* seeing its portal return. **Retrospective evidence** means a later model or explanation fitted with already available results. Unsubmitted candidates do not receive invented scores.
- A public leaderboard snapshot after Round 9 reported rank **1st on F8, 7th on F4, 10th on F7 and 29th on F6** among 39 participants. Rankings compare achieved scores, not verified input vectors, and are historical context only.
- Limited externally published observations informed supplementary exploration of F1/F3/F6, F5/F7 challenger models and five F8 structural corroboration checks. Those records were **never counted as my own portal observations**. The source types and limitations were documented in the [original Round 10 decision audit](journey/round_10/README.md).
- **F8 chronology:** fit a quadratic on the accumulated observations available before Round 10; compare five external responses; submit the predicted vertex; receive a score of 10. Only **later** did I refit using the original 40 supplied observations alone and test it on 13 subsequent personal returns.
- Resolved gap: the R11 F7 coordinates were confirmed from the official results email. A Round 12 F2/F3/F6 shortlist was superseded before final submission; unsubmitted alternatives have no invented portal scores.
- Figure provenance is explained in [the function guide](docs/functions.md): F5/F7/F8 show fixed-coordinate mathematical slices. F1/F2/F3/F4/F6 retain the observed-only charts, and F1 now has **separate, explicitly labelled retrospective reconstructed-model plots**, not portal observations. The new [F1 numerical check](src/bbo/f1_reconstruction.py) uses only 10 supplied F1 rows for coefficient fitting and the 13 personal portal rows for hold-out evaluation; no peer observations enter that experiment.

External source use remains subject to the programme's collaboration and attribution rules. The complete redistribution position is stated in [USAGE_AND_PERMISSIONS.md](USAGE_AND_PERMISSIONS.md).

## 9. Maintenance and reproducibility

The [full CSV](data/all_observations.csv) is the final complete record. Earlier dated CSVs, forecasts and assessed submissions are retained as historical snapshots. The [Jupyter walkthrough](notebooks/Capstone_Final_Walkthrough.ipynb) verifies counts, chronology, final bests and the F5/F8 structural checks. [Automated tests](tests/) and [GitHub Actions](https://github.com/tatonsyML/bbo-capstone-imperial-college/actions/workflows/core-tests.yml) provide independent verification.

**Maintainer:** repository owner. Update only against new authoritative portal or course evidence, with a recorded source and a descriptive commit.

[← Project home](README.md)
