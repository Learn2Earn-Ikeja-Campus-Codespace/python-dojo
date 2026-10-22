"""
Unit tests for Drill 20: Empirical Growth Benchmark Harness
"""
import unittest
from exercise import measure_growth_ratio


class TestBenchmarkHarness(unittest.TestCase):

    def test_linear_growth_ratio(self):
        def linear_task(lst):
            return [x * 2 for x in lst]

        # For double size, ratio should be around 2.0 (allow loose tolerance due to CPU scheduling)
        ratio = measure_growth_ratio(linear_task, 50000, 100000)
        self.assertGreater(ratio, 1.2)
        self.assertLess(ratio, 3.5)


if __name__ == "__main__":
    unittest.main()
