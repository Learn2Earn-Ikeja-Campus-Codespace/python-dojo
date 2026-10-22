"""
Unit tests for Drill 16: Longest Consecutive Sequence
"""
import ast
import inspect
import unittest
from exercise import longest_consecutive


class TestLongestConsecutive(unittest.TestCase):

    def test_consecutive_sequences(self):
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_empty_and_single(self):
        self.assertEqual(longest_consecutive([]), 0)
        self.assertEqual(longest_consecutive([10]), 1)

    def test_no_sorting(self):
        source = inspect.getsource(longest_consecutive)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, ["sorted"], "sorted() is O(n log n). Must be strictly O(n).")


if __name__ == "__main__":
    unittest.main()
