"""
Unit tests for Drill 09: Boyer-Moore Majority Vote
"""
import ast
import inspect
import unittest
from exercise import majority_element


class TestBoyerMoore(unittest.TestCase):

    def test_majority_elements(self):
        self.assertEqual(majority_element([3, 2, 3]), 3)
        self.assertEqual(majority_element([2, 2, 1, 1, 1, 2, 2]), 2)
        self.assertEqual(majority_element([1]), 1)

    def test_no_forbidden_space(self):
        source = inspect.getsource(majority_element)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            if isinstance(node, (ast.Dict, ast.Set, ast.ListComp, ast.DictComp, ast.SetComp)):
                self.fail("Auxiliary data structures forbidden. Boyer-Moore uses O(1) space.")


if __name__ == "__main__":
    unittest.main()
