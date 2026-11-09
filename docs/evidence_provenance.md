# Evidence provenance and academic-use boundaries

**Initial data:** 175 course-provided input-output observations, not personally chosen evaluations.

**Own portal returns:** 13 rounds × 8 functions = 104 outputs, including repeated inputs, giving 279 observed evaluations. The [Round 11/12 log](../data/portal_rounds_11_12.csv) and [Round 13 log](../data/portal_rounds_13.csv) records actual submitted points where sourced.

**Public leaderboard:** its after-Round-9 snapshot ranked this project first on F8, seventh on F4, tenth on F7 and 29th on F6 among 39 participants. It generally showed *attained scores*, not the inputs needed to achieve them.

**Externally published observations:** limited public input-output records informed some later F1, F3 and F6 queries and F5/F7 challenger models; five external F8 records supported a fitted quadratic before the Round 10 submission. They were never counted as this author's portal queries. Source categories and methodological cautions are retained in the [anonymised Round 10 audit](../reports/round10_revision_audit.md). Identifying source citations are excluded from the published repository and should be supplied separately if programme rules require them.

**F8 provenance:** fit on accumulated personal records → check against five public external returns → submit model vertex → receive portal score 10 → later refit on the original 40 supplied course records alone → check against 13 later personal outputs. The final refit is *retrospective*, not a prior prospective decision.

**Evidence distinctions:** recorded pre-outcome predictions are prospective; later reconstructions are retrospective; fitted candidate scores are not achieved portal outcomes; scores from other participants are not added to the author's observation count. External observations may be adaptively selected and are not necessarily unbiased validation samples.

**Known gaps:** Round 11 F7's exact input coordinate was not found in the retained portal audit (its output is verified); Round 12's previously proposed F2/F3/F6 candidate shortlist was not the set actually submitted. Round 13 portal outputs are now included separately in the verified final-round record.

The historical model-card and datasheet documents retain their old time-specific statements. Their “Round 10 pending” language refers to an archived snapshot and does not override the current README.

Public availability of third-party inputs does not override programme collaboration or attribution rules.

## How the visual gallery represents evidence

The [visual gallery](visual_gallery.md) contains model-evaluated surfaces only for the documented F5, F7 and F8 reconstructions. For F1/F2/F3/F4/F6 it shows measured points without interpolation. For F3/F4/F6 the x1–x2 charts are **projections**, not slices with other inputs fixed.

There are **278 plottable input/output pairs** despite **279 returned or supplied evaluations**. The R11 F7 output is recorded but its input is not, so no location is invented. [Figure manifest](../reports/figures/gallery_manifest.json) · [Generator](../scripts/build_visual_gallery.mjs).
