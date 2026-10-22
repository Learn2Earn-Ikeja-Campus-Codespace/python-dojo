"""
Unit tests for Drill 11: Moving Average
"""
import unittest
from exercise import MovingAverage


class TestMovingAverage(unittest.TestCase):

    def test_sliding_window_averages(self):
        ma = MovingAverage(3)
        self.assertAlmostEqual(ma.next(1), 1.0)
        self.assertAlmostEqual(ma.next(10), 5.5)
        self.assertAlmostEqual(ma.next(3), 14 / 3)
        self.assertAlmostEqual(ma.next(5), 6.0) # (10 + 3 + 5) / 3


if __name__ == "__main__":
    unittest.main()
