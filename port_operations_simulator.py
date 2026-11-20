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
        if (isinstance(self.arrival_hour, bool) or not isinstance(self.arrival_hour, (int, float))
                or not math.isfinite(self.arrival_hour)):
            raise ValueError("arrival_hour must be finite")
        if (isinstance(self.service_hours, bool) or not isinstance(self.service_hours, (int, float))
                or not math.isfinite(self.service_hours) or self.service_hours <= 0):
            raise ValueError("service_hours must be finite and positive")


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
    if not isinstance(vessels, list) or any(not isinstance(vessel, Vessel) for vessel in vessels):
        raise ValueError("vessels must be a list of Vessel values")
    names = [vessel.name for vessel in vessels]
    if len(set(names)) != len(names):
        raise ValueError("vessel names must be unique")
    available = [0.0] * berths
    assignments: list[BerthAssignment] = []

    for vessel in sorted(vessels, key=lambda v: (v.arrival_hour, v.name)):
        berth = min(range(berths), key=lambda i: available[i])
        start = max(vessel.arrival_hour, available[berth])
        finish = start + vessel.service_hours
        if not math.isfinite(finish):
            raise OverflowError("berth finish time is not finite")
        if finish <= start:
            raise OverflowError("service interval is below floating-point time resolution")
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
