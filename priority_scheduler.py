from __future__ import annotations

from dataclasses import dataclass
import math

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
    if not isinstance(vessels, list) or any(not isinstance(vessel, PriorityVessel) for vessel in vessels):
        raise ValueError("vessels must be a list of PriorityVessel values")
    pending = list(vessels)
    for vessel in pending:
        if not isinstance(vessel.name, str) or not vessel.name.strip():
            raise ValueError("vessel name must be non-empty")
        if (isinstance(vessel.arrival_hour, bool) or not isinstance(vessel.arrival_hour, (int, float))
                or not math.isfinite(vessel.arrival_hour)):
            raise ValueError("arrival_hour must be finite")
        if (isinstance(vessel.service_hours, bool) or not isinstance(vessel.service_hours, (int, float))
                or not math.isfinite(vessel.service_hours) or vessel.service_hours <= 0):
            raise ValueError("service_hours must be finite and positive")
        if isinstance(vessel.priority, bool) or not isinstance(vessel.priority, int):
            raise ValueError("priority must be an integer")
    names = [v.name for v in pending]
    if len(names) != len(set(names)):
        raise ValueError("vessel names must be unique")
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
        if not math.isfinite(finish):
            raise OverflowError("berth finish time is not finite")
        if finish <= start:
            raise OverflowError("service interval is below floating-point time resolution")
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
