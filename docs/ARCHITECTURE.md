# Architecture

Vessel arrival stream → berth availability state → earliest-available allocation → service completion → waiting-time/utilization summary.

## Invariants
1. A berth cannot serve overlapping vessels.
2. Service cannot start before arrival.
3. Increasing parallel berth capacity should not create artificial extra waiting in identical cases.
