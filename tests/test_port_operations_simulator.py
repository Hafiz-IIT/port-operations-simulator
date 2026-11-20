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
        for value in (0, -1, 1.5, True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    schedule([], value)

    def test_invalid_vessel_times_are_rejected(self):
        with self.assertRaises(ValueError):
            Vessel("A", float("nan"), 1)
        with self.assertRaises(ValueError):
            Vessel("A", 0, -1)

    def test_boolean_and_nonfinite_times_are_rejected(self):
        with self.assertRaises(ValueError):
            schedule([Vessel("A", True, 1)], berths=1)
        with self.assertRaises(ValueError):
            schedule([Vessel("A", 0, float("nan"))], berths=1)

    def test_positive_service_duration_below_time_resolution_is_rejected(self):
        with self.assertRaises(OverflowError):
            schedule([Vessel("A", 1e16, 1.0)], berths=1)

    def test_duplicate_vessel_names_are_rejected(self):
        with self.assertRaises(ValueError):
            schedule([Vessel("A", 0, 1), Vessel("A", 2, 1)], 1)


if __name__ == "__main__":
    unittest.main()
