# Port Operations Simulator

> Discrete berth-allocation simulator for vessel arrivals, service times, queueing delay and berth utilization.

## Status
**Reproducible simulation/research prototype** with executable code, tests, CI, architecture, evaluation and roadmap documentation.

## Problem
Port congestion emerges from arrival timing, limited berth capacity and service duration. A small simulator makes queueing effects and allocation policies measurable.

## Architecture
Vessel arrival stream → berth availability state → earliest-available allocation → service completion → waiting-time/utilization summary.

## Quick start
```bash
python -m unittest discover -s tests -v
python port_operations_simulator.py
```

## Implemented
- Vessel model
- Multiple berth state
- Earliest-available allocation
- Wait-time calculation
- Assignment records
- Aggregate wait summary
- Tests and CI

## Research lineage
- *Smart Urban Infrastructures: AI-Enabled City Optimization*
- *Multi-Agent Coordination via Linear Statistical Models and Reinforcement Learning*
- *Reinforcement-Driven Optimization in Industrial AI*

## Evaluation
Current tests compare single vs parallel berth behavior and enforce non-overlap; later experiments can benchmark alternative scheduling policies.

## Limitations
- Greedy deterministic scheduler
- No crane/tide/channel constraints
- No AIS or real port data
- No production terminal integration

## License
MIT.

## Extended implementation

- `priority_scheduler.py` adds non-preemptive priority scheduling for vessels waiting for a berth.
