"""
Unit tests for Drill 19: Subarrays Summing to K
"""
import unittest
from exercise import subarray_sum


class TestSubarraySum(unittest.TestCase):

    def test_subarray_counts(self):
        self.assertEqual(subarray_sum([1, 1, 1], 2), 2)
        self.assertEqual(subarray_sum([1, 2, 3], 3), 2)
        self.assertEqual(subarray_sum([1, -1, 0], 0), 3)

    def test_no_matches(self):
        self.assertEqual(subarray_sum([1, 2, 3], 10), 0)


if __name__ == "__main__":
    unittest.main()
