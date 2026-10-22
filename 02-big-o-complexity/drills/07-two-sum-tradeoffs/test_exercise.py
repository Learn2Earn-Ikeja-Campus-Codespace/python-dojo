"""
Unit tests for Drill 07: Two Sum Hash
"""
import unittest
from exercise import two_sum_hash


class TestTwoSum(unittest.TestCase):

    def test_found_pairs(self):
        res = two_sum_hash([2, 7, 11, 15], 9)
        self.assertIn(res, [(0, 1), (1, 0)])

        res = two_sum_hash([3, 2, 4], 6)
        self.assertIn(res, [(1, 2), (2, 1)])

    def test_duplicate_values(self):
        res = two_sum_hash([3, 3], 6)
        self.assertIn(res, [(0, 1), (1, 0)])

    def test_not_found(self):
        self.assertIsNone(two_sum_hash([1, 2, 3], 10))


if __name__ == "__main__":
    unittest.main()
