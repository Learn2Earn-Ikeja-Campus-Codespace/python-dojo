"""
Unit tests for Drill 18: Trapping Rain Water
"""
import unittest
from exercise import trap


class TestTrappingRainWater(unittest.TestCase):

    def test_trapped_water(self):
        self.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(trap([4, 2, 0, 3, 2, 5]), 9)

    def test_flat_and_monotone(self):
        self.assertEqual(trap([1, 1, 1]), 0)
        self.assertEqual(trap([3, 2, 1]), 0)
        self.assertEqual(trap([]), 0)


if __name__ == "__main__":
    unittest.main()
