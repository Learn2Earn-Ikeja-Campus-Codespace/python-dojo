"""
Unit tests for Drill 14: Generate All Subsets
"""
import ast
import inspect
import unittest
from exercise import subsets


class TestGenerateSubsets(unittest.TestCase):

    def test_subsets_count_and_content(self):
        res = subsets([1, 2, 3])
        self.assertEqual(len(res), 8) # 2^3
        # Normalize to sorted tuples for comparison
        normalized = {tuple(sorted(s)) for s in res}
        expected = {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}
        self.assertEqual(normalized, expected)

    def test_empty_list(self):
        self.assertEqual(subsets([]), [[]])

    def test_single_element(self):
        res = subsets([7])
        self.assertEqual(len(res), 2)
        self.assertIn([], res)
        self.assertIn([7], res)

    def test_no_loops_or_itertools(self):
        source = inspect.getsource(subsets)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops forbidden.")


if __name__ == "__main__":
    unittest.main()
