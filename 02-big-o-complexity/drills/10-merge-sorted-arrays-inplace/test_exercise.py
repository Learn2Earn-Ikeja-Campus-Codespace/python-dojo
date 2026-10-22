"""
Unit tests for Drill 10: In-Place Merge
"""
import unittest
from exercise import merge_inplace


class TestInPlaceMerge(unittest.TestCase):

    def test_standard_merge(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        merge_inplace(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_nums2_empty(self):
        nums1 = [1]
        nums2 = []
        merge_inplace(nums1, 1, nums2, 0)
        self.assertEqual(nums1, [1])

    def test_nums1_initial_empty(self):
        nums1 = [0]
        nums2 = [1]
        merge_inplace(nums1, 0, nums2, 1)
        self.assertEqual(nums1, [1])


if __name__ == "__main__":
    unittest.main()
