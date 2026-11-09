# Round 8 | recorded forecasts and returned evidence

**Evidence status:** The original inputs and portal returns are retained in [queries.txt](queries.txt) and [outputs.txt](outputs.txt). The forecasts below were recorded *before* the return, making them useful checks rather than retrospective fits.

| Function | Prospective prediction recorded | Why it mattered |
|---|---:|---|
| F2 | Local quadratic ≈ 0.695189 at `0.701500-0.959720` | Test whether a narrow local model was reliable |
| F3 | Local-path ≈ −0.019675 | Check another near-incumbent direction |
| F5 | Local quadratic ≈ 5654.123 | Test whether the trend towards larger values persisted |
| F7 | Local quadratic ≈ 1.791396 | Challenge the existing regional model |
| F8 | Three GP-kernel predictions ≈ 9.902821, 9.906066, 9.907368 | Compare model agreement instead of trusting one kernel |

F1, F4 and F6 had **no reliable scalar forecast recorded**. I have not invented one. The numerical source history provides the returned outcomes, and the [project journey](../../docs/project_journey.md) places the experiment within the wider search.

**Lesson:** even a plausible local model must be tested against new portal evidence before it directs the next limited query. This is a historical forecast audit, not proof of a solved function.
