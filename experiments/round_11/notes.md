# Week 11 proposal — NOT YET SUBMITTED

This records candidate input coordinates, not returned scores. Confirmed Week 10 observations were incorporated into the decision. The valid range is 0.000000–0.999999 inclusive at six-decimal precision, per the official capstone FAQ.

**Method:** Three local Matérn 5/2 GP fits using different length scales and regularisation/noise assumptions around promising regions, using the participant’s historical observations and labelled external examples from public peer repositories. These are **not** executions of the official HEBO package or adaptive TuRBO. Their interpretation is exploratory because peer data are selected adaptively and the local models are not independently validated.

**Proposals (not submitted):**
- F1: `0.628540-0.628540`
- F2: `0.692000-0.366000`
- F3: `0.445500-0.593000-0.420000`
- F4: `0.415000-0.417000-0.366500-0.413000`
- F5: `0.999999-0.999999-0.999999-0.999998`
- F6: `0.457000-0.370000-0.642000-0.738000-0.020000`
- F7: `0.233000-0.128000-0.522000-0.276000-0.310000-0.667000`
- F8: `0.100000-0.150000-0.130000-0.150000-0.800000-0.500000-0.200000-0.600000`

**Why:** F1 targets a peer-observed high-response region; F2 challenges a stronger alternative F2 basin; F3, F4, F6 and F7 make model-guided local moves near better externally observed regions; F5 tests a distinct legal near-boundary point after attaining 8662.405; F8 reuses the personally achieved, structurally recovered 10-point vertex. No proposed score is claimed as measured. External observations are attributed as peer evidence and not added to this participant’s own evaluation history.

**Important:** Before marking these as submitted, the participant must confirm the portal entry and the course's academic collaboration rules. Once a score arrives, record it without overwriting historical forecasts.
