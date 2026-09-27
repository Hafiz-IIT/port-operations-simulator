# Port Operations Simulator

> **A transparent berth-allocation baseline for vessel arrivals, queues, service time, and waiting-time analysis.**

Port congestion and berth allocation affect downstream logistics, but a credible project should start with a reproducible scheduling baseline before claiming a real port digital twin. This repo models the queueing/scheduling core.

## Implemented
- vessel arrival/service model
- configurable berth count
- earliest-available berth assignment
- start/finish times
- per-vessel wait time
- average/max wait summary

## Run
```bash
python -m unittest discover -s tests -v
python port_operations_simulator.py
```

## Repository map
`port_operations_simulator.py` core · `tests/` tests · `examples/` fixtures · `docs/architecture.md` design · `docs/research-agenda.md` experiments · `STATUS.md` claims · `CITATION.cff` citation

## Pipeline
**vessels → arrival ordering → berth availability → assignment → service schedule → wait metrics**

## Research lineage
This comes from the older port optimization, scheduling, logistics digital twin, cargo allocation, and EXIM operations themes.

## Evaluation direction
Compare berth counts, arrival bursts, service-time distributions, and alternative scheduling heuristics. Later add priorities or stochastic delays rather than presenting the greedy baseline as optimal.

## Maturity
**Research prototype.** Synthetic scheduling only. No real port/AIS feed, terminal operating system, customs state, crane constraints, or operational optimization claim.
