# Research decisions and evidence ledger

1. **Verified scope** — both uploaded papers concern chained tool-call failure modes and oversight. The original manuscript describes error propagation, review distinguishes checkpoint placement as unresolved. Evidence: supplied student papers (original §§3, 7; review §7).
2. **Selected problem** — compare checkpoint placement policies in reproducible synthetic tool chains. Rationale: narrow enough to execute without GPUs, external API access or third-party data. Status: INFERRED design, not a published novelty claim.
3. **Pathway** — controlled comparative study (assignment pathway B). Controls: same generated scenarios, fault rates, detection probability, seeds and metrics for all policies. Status: VERIFIED by code and configuration.
4. **Metrics frozen** — strict success (clean final state and no unsafe high-risk action), unsafe-run rate, review counts. Status: VERIFIED via simulator and CSV.
5. **Three controls** — no verification, fixed every four actions after execution, risk-adaptive before high-risk actions. The timing difference is a designed comparison feature and limitation, not hidden.
6. **Five seeds** — 11, 29, 47, 83, 101; 400 scenarios per seed and length; same scenario reused across the three policies. Status: VERIFIED in protocol and runs.
7. **Deeper analysis** — sweep risk-recognition recall (0.5/0.75/1.0). Status: VERIFIED in sensitivity.csv.
8. **Evidence-preserving publication** — claims restricted to simulated behavior. No LLM model, real API, real human or recovered benchmark performance was tested. Status: VERIFIED design limit.
9. **Authorship/accountability** — AI generated/ran code and assisted manuscript drafting; submitting student should independently inspect, rerun and revise. No unobserved student decisions are attributed to them.
10. **Source verification** — bibliography titles and venues inherited from the supplied manuscripts; independent metadata verification remains TO VERIFY before broader release.

## Questions
- RQ1: What are strict success rates under each policy and length?
- RQ2: What is the unsafe-action reduction versus review burden?
- RQ3: What happens if risk recognition recall is lowered?

## Chosen minimum viable implementation
A pure-Python deterministic state machine. The baseline is the no-checkpoint policy; alternatives retain identical state transitions and differ only in checkpoint rule. Paired fault streams limit confounding from scenario severity, although policy timing is intrinsically different.
