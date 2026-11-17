# Baseline validation (G2)

**Baseline**: synthetic chained tool workflow with no human checkpoints. This is a baseline built for the study, NOT a reproduction of published WebArena, AgentDojo or any other research result.

**VERIFIED**: `python scripts/test_simulator.py` exited successfully with `PASS: deterministic replay, policy review counts, clean workflow, irreversible-action safety`. Determinism, zero baseline reviews, correct number of fixed periodic checks, clean-workflow success and an unsafe irreversible-action edge case were checked.

**VERIFIED**: `python scripts/run_experiments.py` produced 18,000 primary run rows and aggregate results. At length 24, no-checkpoint strict success was 0.1500 across 2,000 scenarios and mean reviews exactly 0.

**UNCERTAIN**: The selected injection/detection probabilities are design assumptions, not calibrated against original published agent trace data. Outcomes depend on these values.

**NEEDS CORRECTION before empirical deployment**: use external tool-trace benchmarks, observe real reviewer errors, use identical pre-action timing where appropriate, and report uncertainty intervals under independent sampling.

**Validation rationale**: terminal-state cleanup is not sufficient to count as task success after an unsafe action. A specific edge case in `test_simulator.py` verifies that the unsafe action remains counted after recovery.
