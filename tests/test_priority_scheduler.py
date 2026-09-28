import unittest

from priority_scheduler import PriorityVessel, schedule_single_berth_priority


class PrioritySchedulerTests(unittest.TestCase):
    def test_priority_applies_to_waiting_vessels(self):
        vessels = [
            PriorityVessel("A", 0, 4, priority=0),
            PriorityVessel("B", 1, 2, priority=1),
            PriorityVessel("C", 1, 2, priority=5),
        ]
        names = [a.vessel for a in schedule_single_berth_priority(vessels)]
        self.assertEqual(names, ["A", "C", "B"])

    def test_does_not_start_before_arrival(self):
        assignment = schedule_single_berth_priority(
            [PriorityVessel("A", 10, 2, priority=1)]
        )[0]
        self.assertEqual(assignment.start_hour, 10)


if __name__ == "__main__":
    unittest.main()
