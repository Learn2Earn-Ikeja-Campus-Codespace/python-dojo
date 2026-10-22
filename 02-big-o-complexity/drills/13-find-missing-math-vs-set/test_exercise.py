"""
Unit tests for Drill 13: Find Missing Number
"""
import ast
import inspect
import unittest
from exercise import find_missing_number


class TestFindMissingNumber(unittest.TestCase):

    def test_missing_numbers(self):
        self.assertEqual(find_missing_number([3, 0, 1]), 2)
        self.assertEqual(find_missing_number([0, 1]), 2)
        self.assertEqual(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_no_extra_space(self):
        source = inspect.getsource(find_missing_number)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            if isinstance(node, (ast.Set, ast.Dict, ast.SetComp, ast.DictComp)):
                self.fail("Sets/Dicts forbidden. Use O(1) space mathematical invariant.")


if __name__ == "__main__":
    unittest.main()
