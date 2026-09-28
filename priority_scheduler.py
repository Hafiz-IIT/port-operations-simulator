from __future__ import annotations

from dataclasses import dataclass

from port_operations_simulator import BerthAssignment


@dataclass(frozen=True)
class PriorityVessel:
    name: str
    arrival_hour: float
    service_hours: float
    priority: int = 0


def schedule_single_berth_priority(vessels: list[PriorityVessel]) -> list[BerthAssignment]:
    """Non-preemptive single-berth priority scheduling.

    Higher numeric priority wins among vessels that have already arrived.
    If no vessel is waiting, time advances to the next arrival.
    """
    pending = list(vessels)
    current = 0.0
    assignments: list[BerthAssignment] = []

    while pending:
        arrived = [v for v in pending if v.arrival_hour <= current]
        if not arrived:
            current = min(v.arrival_hour for v in pending)
            arrived = [v for v in pending if v.arrival_hour <= current]

        vessel = min(
            arrived,
            key=lambda v: (-v.priority, v.arrival_hour, v.name),
        )
        start = max(current, vessel.arrival_hour)
        finish = start + vessel.service_hours
        assignments.append(
            BerthAssignment(
                vessel=vessel.name,
                berth=0,
                start_hour=start,
                finish_hour=finish,
                wait_hours=start - vessel.arrival_hour,
            )
        )
        current = finish
        pending.remove(vessel)

    return assignments
