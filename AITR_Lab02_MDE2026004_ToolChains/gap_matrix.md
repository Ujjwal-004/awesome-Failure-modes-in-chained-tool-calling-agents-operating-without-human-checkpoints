# Research gap matrix — source-to-test mapping

**Source A:** Supplied original manuscript, *Failure Modes in Chained Tool-Calling Agents Operating Without Human Checkpoints*, Ujjwal Gupta, pages 3–6: failure taxonomy, error propagation, safeguards, research gaps. **Source B:** Supplied review manuscript, same topic, sections 6–7: limitations and research agenda. These are student manuscripts, not independent experimental evidence.

| Candidate gap | Source evidence | Type | Testable question | Feasible experiment | Status / ranking |
|---|---|---|---|---|---|
| Checkpoint placement | Review §7.3 identifies unclear placement; original §7.1 argues for risk-adaptive checkpoints | Source-identified open question | When does risk-guided checking outperform periodic checking? | Controlled fault injection, three checkpoint policies | Selected, rank 1 |
| Chain-level failure measurement | Review §7.1 calls for failure-annotated benchmarks; original §7.8 advocates chain-level measures | Source-identified open question | Does terminal state success hide earlier unsafe actions? | Log strict success vs. end-state cleanliness and unsafe-action count | Included, rank 2 |
| Causal propagation and recovery | Review §7.2 identifies insufficient causal trace-back; original §3.5 describes compounding errors | Source-identified open question | How often can a checkpoint repair persistent corruption? | Track injected faults and recovery counts | Included, rank 3 |
| Imperfect risk detection | Review §7.4 says probabilistic safeguards have weak guarantees | Inferred experimental extension | How does detector recall change safety/cost? | Recall sensitivity sweep | Included, rank 4 |
| Realistic prompt-injection/tool composition | Review §§7.5, 4.5–4.6; original §§3.9–3.12 | Source-identified open question | How do adversarial and permission effects interact? | AgentDojo or realistic simulator benchmark | Not tested; rank 5, beyond available scope |

**Evidence classification:** VERIFIED = section text appears in the uploaded documents or metrics came from executed scripts. INFERRED = specific simulated policy choice; its real-world efficacy is not externally verified. UNKNOWN = published novelty, real-user detection rates and whether risk distributions match live agents.

**Novelty caveat:** These gaps are identified within the supplied student manuscripts; no claim is made that the global literature has never examined checkpoint policies.
