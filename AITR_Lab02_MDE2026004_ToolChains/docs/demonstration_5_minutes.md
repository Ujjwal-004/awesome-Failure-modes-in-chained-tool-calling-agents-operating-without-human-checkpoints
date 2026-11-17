# Five-minute demonstration script (G4)

0:00–0:45 — Identify the source topic, the original paper's propagation thesis and the review's checkpoint-placement gap.

0:45–1:30 — Open `src/simulator.py`. Explain `corrupted`, high-risk actions, injection probabilities and why an unsafe action cannot be erased by later recovery.

1:30–2:15 — Open `configs/protocol.json`. Explain the 6/12/24 action lengths, five seeds, matched scenarios, and three policies.

2:15–3:00 — Run `python scripts/test_simulator.py`, then `python scripts/run_experiments.py` and show `results/results.csv`.

3:00–4:00 — Open the graphs: 24-step strict success 15.00% (none), 22.35% (fixed), 24.70% (adaptive); adaptive has fewer unsafe runs but more reviews.

4:00–5:00 — Explain recall sensitivity (0.5 -> 1.0), why no live LLM was evaluated and what a real benchmark would require. Be prepared to discuss verification timing as a confound.
