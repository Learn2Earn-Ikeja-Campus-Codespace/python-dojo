"""
Unit tests for Drill 15: String Permutations
"""
import ast
import inspect
import unittest
from exercise import permutations


class TestStringPermutations(unittest.TestCase):

    def test_permutations_abc(self):
        res = permutations("abc")
        self.assertEqual(len(res), 6) # 3!
        self.assertEqual(set(res), {"abc", "acb", "bac", "bca", "cab", "cba"})

    def test_single_and_empty(self):
        self.assertEqual(permutations("a"), ["a"])
        self.assertEqual(permutations(""), [""])

    def test_type_error(self):
        with self.assertRaises(TypeError):
            permutations(123)

    def test_no_itertools(self):
        source = inspect.getsource(permutations)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            if isinstance(node, ast.Attribute) and node.attr == "permutations":
                self.fail("itertools is forbidden.")


if __name__ == "__main__":
    unittest.main()
