# Authentic AI assistance and verification log

Date: 2026-11-14. This file documents assistant actions and reproducible tool outputs from this session. It does not invent a human student's prompts, approvals, commits or manual debug actions.

| Stage | AI support / proposal | Verification performed | Result / outstanding check |
|---|---|---|---|
| Paper reading | Mapped source taxonomies to checkpoint-placement questions | Inspected attached original/review and assignment text | Selected narrow synthetic system study; external novelty unresolved |
| Experimental design | Proposed no-check, fixed post-action, and risk-adaptive checks | Frozen `configs/protocol.json` and implemented deterministic paired scenarios | Real fault-injection results, not simulated logs |
| Initial evaluation | Noted that post-action adaptive review could not prevent previously unsafe high-risk actions | Inspected preliminary executed output, in which adaptive strict success equaled no-checkpoint success | Corrected policy timing to pre-action for adaptive, reran all trials and graphs; old results are NOT part of final evidence |
| Unit checks | Proposed deterministic replay, review-count tests and unsafe-action test | Executed `python scripts/test_simulator.py` | Tests passed |
| Experiments | Generated primary and recall-sensitivity CSVs | Executed `python scripts/run_experiments.py`, inspected console results | 18,000 primary rows; 18,000 sensitivity runs |
| Visualization | Generated charts from saved CSVs | Executed `python scripts/make_figures.py`; figure files created | Four figure families (PNG and PDF) |
| Paper drafting | Produced LaTeX manuscript from observed numeric results | Built with pdflatex and copied resulting PDF | 6-page PDF; bibliographic metadata copied from source papers, external verification needed |

## AI limitations and corrections actually observed
1. First checkpoint timing made adaptive verification incapable of reversing already-unsafe actions. It was revised to pre-action and the experiment was fully rerun.
2. The local environment had `pdflatex` but not `bibtex`; a self-contained bibliography was added to the manuscript while retaining the `.bib` export.
3. Simulator conclusions cannot support an assertion about a specific deployed LLM. The draft explicitly limits conclusions to synthetic trials.

**Student verification required:** inspect source code, reproduce results independently, audit original citations, confirm the model assumptions are defensible and prepare the demonstration. AI support is disclosed; no human validation not actually performed is claimed.
