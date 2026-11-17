from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Vessel:
    name: str
    arrival_hour: float
    service_hours: float

    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("vessel name is required")
        if not math.isfinite(self.arrival_hour) or not math.isfinite(self.service_hours):
            raise ValueError("arrival and service times must be finite")
        if self.service_hours < 0:
            raise ValueError("service_hours must be non-negative")


@dataclass(frozen=True)
class BerthAssignment:
    vessel: str
    berth: int
    start_hour: float
    finish_hour: float
    wait_hours: float


def schedule(vessels: list[Vessel], berths: int) -> list[BerthAssignment]:
    if not isinstance(berths, int) or isinstance(berths, bool) or berths < 1:
        raise ValueError("berths must be a positive integer")
    names = [vessel.name for vessel in vessels]
    if len(set(names)) != len(names):
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
