from __future__ import annotations

from dataclasses import dataclass


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
    if berths < 1:
        raise ValueError("berths must be >= 1")
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
