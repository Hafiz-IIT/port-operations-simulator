from __future__ import annotations

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Vessel:
    name: str
    arrival_hour: float
    service_hours: float


@dataclass(frozen=True)
class BerthAssignment:
    vessel: str
    berth: int
    start_hour: float
    finish_hour: float
    wait_hours: float


def schedule(vessels: list[Vessel], berths: int) -> list[BerthAssignment]:
    if isinstance(berths, bool) or not isinstance(berths, int) or berths < 1:
        raise ValueError("berths must be a positive integer")
    for vessel in vessels:
        if not isinstance(vessel.name, str) or not vessel.name.strip():
            raise ValueError("vessel name must be non-empty")
        if (isinstance(vessel.arrival_hour, bool) or
                not isinstance(vessel.arrival_hour, (int, float)) or
                not isfinite(vessel.arrival_hour)):
            raise ValueError("arrival_hour must be finite")
        if (isinstance(vessel.service_hours, bool) or
                not isinstance(vessel.service_hours, (int, float)) or
                not isfinite(vessel.service_hours) or vessel.service_hours <= 0):
            raise ValueError("service_hours must be finite and positive")
    names = [v.name for v in vessels]
    if len(names) != len(set(names)):
        raise ValueError("vessel names must be unique")
    available = [0.0] * berths
    assignments: list[BerthAssignment] = []

    for vessel in sorted(vessels, key=lambda v: (v.arrival_hour, v.name)):
        berth = min(range(berths), key=lambda i: available[i])
        start = max(vessel.arrival_hour, available[berth])
        finish = start + vessel.service_hours
        assignments.append(
            BerthAssignment(
                vessel=vessel.name,
                berth=berth,
                start_hour=start,
                finish_hour=finish,
                wait_hours=start - vessel.arrival_hour,
            )
        )
        available[berth] = finish
    return assignments


def summary(assignments: list[BerthAssignment]) -> dict:
    if not assignments:
        return {"vessels": 0, "average_wait_hours": 0.0, "max_wait_hours": 0.0}
    waits = [a.wait_hours for a in assignments]
    return {
        "vessels": len(assignments),
        "average_wait_hours": sum(waits) / len(waits),
        "max_wait_hours": max(waits),
    }


if __name__ == "__main__":
    vessels = [Vessel("A", 0, 4), Vessel("B", 1, 2), Vessel("C", 2, 3)]
    print(schedule(vessels, berths=2))
