# Frozen experiment protocol — G3

See `configs/protocol.json` for exact values. No human checkpoints are executed in the real world: a simulated reviewer intercepts before high-risk actions (adaptive) or after every four actions (fixed).

```
Synthetic seeded chain -> step risk label -> optional adaptive pre-check
                     -> stochastic fault injection -> tool state update
                     -> record unsafe high-risk execution
                     -> optional periodic post-check -> next step
                     -> log strict success, unsafe exposure, reviews and recovery
```

**Frozen inputs:** chain lengths 6/12/24; seeds 11/29/47/83/101; 400 trials per seed and length; high-risk frequency 0.30; low/high action fault probability 0.035/0.17; reviewer detection 0.92; fixed interval 4.

**Outputs:** per-trial CSV, aggregated CSV and PNG/PDF line plots. **Primary metric direction:** strict success higher is better; unsafe-run rate and review effort lower are better.

**Deeper analysis:** adaptive risk recognition recall 0.5/0.75/1.0. **Integrity:** no trained or tuned model; same generated exogenous sequence across methods; results are deterministic on rerun given Python-compatible PRNG.

**Potential confounds:** fixed vs adaptive action timing differs. Detector costs assumed equal. Human fatigue, false positives, untrustworthy tool output and genuine rollback not represented.
