# Capstone BBO — Module 19 / Round 8

This package keeps the numerical history separate from the later narrative.

## Contents
- `initial_data/`: original `.npy` arrays for all eight functions.
- `results/submission_history_through_week7.csv`: initial best plus every submitted Week 1–7 query and returned output.
- `results/week7_audit.csv`: what Week 7 confirmed or contradicted, including forecasts recorded before the results.
- `results/round8_queries.csv`: proposed Round 8 queries and rationale.
- `results/round8_portal_values.txt`: portal-ready six-decimal strings.
- `capstone_bbo_module19_round8.py`: reproduces the rank-GP diagnostic for F1, local brackets for F2/F3, the controlled trend diagnostics for F5/F7, the GP-kernel committee check for F8, and duplicate validation for all eight queries.

F4 and F6 are deliberately simple controlled experiments rather than model-generated points: F4 tests one micro-step on the opposite side of the incumbent; F6 tests the symmetric side after a one-microstep change produced a material deterioration.

The decision rule remains evidence-led: use controlled local geometry when it has survived portal feedback; reduce model authority after a forecast failure; and change one variable at a time where the local surface has become difficult to identify.
