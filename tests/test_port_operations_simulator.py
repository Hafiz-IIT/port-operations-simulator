import unittest

from port_operations_simulator import Vessel, schedule, summary


class PortSimulatorTests(unittest.TestCase):
    def test_parallel_berths_reduce_wait(self):
        vessels = [Vessel("A", 0, 4), Vessel("B", 0, 4)]
        one = schedule(vessels, 1)
        two = schedule(vessels, 2)
        self.assertGreater(summary(one)["average_wait_hours"], summary(two)["average_wait_hours"])

    def test_single_berth_does_not_overlap(self):
        assignments = schedule([Vessel("A", 0, 2), Vessel("B", 1, 2)], 1)
        self.assertGreaterEqual(assignments[1].start_hour, assignments[0].finish_hour)

    def test_invalid_berths(self):
        with self.assertRaises(ValueError):
            schedule([], 0)


if __name__ == "__main__":
    unittest.main()
