"""
Unit tests for Drill 12: Matrix Search Elimination
"""
import unittest
from exercise import search_matrix


class TestMatrixSearch(unittest.TestCase):

    def setUp(self):
        self.matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]

    def test_found_targets(self):
        self.assertTrue(search_matrix(self.matrix, 5))
        self.assertTrue(search_matrix(self.matrix, 1))
        self.assertTrue(search_matrix(self.matrix, 30))

    def test_not_found(self):
        self.assertFalse(search_matrix(self.matrix, 20))
        self.assertFalse(search_matrix(self.matrix, -1))
        self.assertFalse(search_matrix(self.matrix, 100))

    def test_empty(self):
        self.assertFalse(search_matrix([], 5))
        self.assertFalse(search_matrix([[]], 5))


if __name__ == "__main__":
    unittest.main()
