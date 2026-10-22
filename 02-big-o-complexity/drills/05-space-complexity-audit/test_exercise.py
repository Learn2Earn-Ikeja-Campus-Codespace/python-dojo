"""
Unit tests for Drill 05: Space Complexity Audit
"""
import unittest
from exercise import reverse_with_allocation, reverse_in_place


class TestSpaceAudit(unittest.TestCase):

    def test_allocation_reversal(self):
        orig = [1, 2, 3, 4]
        copy = list(orig)
        rev = reverse_with_allocation(orig)
        self.assertEqual(rev, [4, 3, 2, 1])
        self.assertEqual(orig, copy, "reverse_with_allocation must NOT mutate the original list!")

    def test_in_place_reversal(self):
        nums = [1, 2, 3, 4, 5]
        res = reverse_in_place(nums)
        self.assertIsNone(res, "reverse_in_place must return None")
        self.assertEqual(nums, [5, 4, 3, 2, 1], "reverse_in_place must mutate nums directly!")

    def test_empty_and_single(self):
        empty = []
        reverse_in_place(empty)
        self.assertEqual(empty, [])


if __name__ == "__main__":
    unittest.main()
