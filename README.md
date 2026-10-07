# Port Operations Simulator

<p align="center"><strong>Berth Allocation, Queueing and Port Congestion</strong><br/><sub>A discrete-event simulation sandbox for measurable berth-policy experiments.</sub></p>

<p align="center"><img src="https://img.shields.io/badge/status-reproducible%20simulation-blue" alt="Simulation"/> <img src="https://img.shields.io/badge/focus-berth%20allocation-orange" alt="Berth allocation"/></p>

## Question

**How do vessel arrivals, service duration and limited berth capacity interact to create waiting time?**

```
Arrival stream
   ↓
Berth availability
   ↓
Allocation policy
   ↓
Service completion
   ↓
Waiting time + utilization
```

## Try it

```bash
python port_operations_simulator.py
python -m unittest discover -s tests -v
```

`priority_scheduler.py` adds a second policy: non-preemptive priority scheduling among vessels already waiting.

## Implemented

- vessel state
- multiple berths
- earliest-available allocation
- waiting-time calculation
- berth assignment records
- priority scheduling
- utilization summaries
- deterministic CI

## Research boundary

Simulation only. Results are not calibrated to a particular port or claimed as operational recommendations.

Related: [Logistics Optimization Lab](https://github.com/Hafiz-IIT/logistics-optimization-lab) · [Multi-Agent Logistics Simulator](https://github.com/Hafiz-IIT/multi-agent-logistics-sim)
