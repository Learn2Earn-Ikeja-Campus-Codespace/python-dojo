"""
Unit tests for Drill 08: Array Intersection
"""
import unittest
from exercise import intersection


class TestArrayIntersection(unittest.TestCase):

    def test_standard_intersection(self):
        self.assertEqual(set(intersection([1, 2, 2, 1], [2, 2])), {2})
        self.assertEqual(set(intersection([4, 9, 5], [9, 4, 9, 8, 4])), {4, 9})

    def test_no_intersection(self):
        self.assertEqual(intersection([1, 2, 3], [4, 5, 6]), [])

    def test_empty(self):
        self.assertEqual(intersection([], [1, 2]), [])


if __name__ == "__main__":
    unittest.main()
