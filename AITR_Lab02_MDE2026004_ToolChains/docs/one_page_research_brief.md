# One-page research brief — G1

**Student:** Ujjwal Gupta (MDE2026004)

**Topic:** Failure Modes in Chained Tool-Calling Agents Operating Without Human Checkpoints.

**Source basis:** original manuscript, especially §§3, 7; review manuscript, especially §§6–7. Review concerns system-level failure propagation and checkpoint risk.

**Specific research gap:** the student papers identify unclear checkpoint placement and insufficient fine-grained measurement of propagation, unsafe exposure and review effort; neither supplied manuscript reports a controlled policy experiment.

**Primary question:** under a fixed synthetic fault process, which of no-checkpoint, fixed-interval post-action or risk-adaptive pre-action checking offers the best safety--review trade-off?

**Contribution type:** controlled comparative simulation, not algorithm discovery or direct published baseline reproduction.

**Data/protocol:** fully synthetic pseudo-random sequential action traces; no external data license, participant data or API calls. Five seeds and three chain lengths. Matched scenarios across policies.

**Comparison methods:** no checkpoint, fixed checks every 4 actions, checks before high-risk actions.

**Primary metric:** strict success (final state clean and zero unsafe actions). Secondary: unsafe-run fraction, mean reviewer actions, recovery, terminal correctness.

**Compute feasibility:** lightweight CPU/standard library; optional matplotlib only for plots. Risk: distribution and perfect labeling unrealistic; sensitivity study reduces risk recall.

**Verified first milestone:** executable state-machine tests passed and baseline produced actual CSV.

**Paper-specific caveat:** external baseline research can inspire questions but is not numerically reproduced here.
