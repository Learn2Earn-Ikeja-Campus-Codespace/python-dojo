"""
Unit tests for Drill 01: Duplicate Detection & Trade-offs
"""
import unittest
from exercise import has_duplicate_quadratic, has_duplicate_hash, has_duplicate_sorted


class TestDuplicateDetection(unittest.TestCase):

    def setUp(self):
        self.no_dups = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.has_dups = [10, 20, 30, 40, 20, 50]
        self.empty = []
        self.single = [42]
        self.early_dup = [7, 7, 1, 2, 3, 4, 5]

    def test_all_approaches(self):
        funcs = [has_duplicate_quadratic, has_duplicate_hash, has_duplicate_sorted]
        for fn in funcs:
            self.assertFalse(fn(self.no_dups))
            self.assertTrue(fn(self.has_dups))
            self.assertFalse(fn(self.empty))
            self.assertFalse(fn(self.single))
            self.assertTrue(fn(self.early_dup))


if __name__ == "__main__":
    unittest.main()
