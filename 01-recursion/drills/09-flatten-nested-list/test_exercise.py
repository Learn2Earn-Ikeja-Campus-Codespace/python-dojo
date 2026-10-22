"""
Unit tests for Drill 09: Flatten Arbitrarily Nested List
"""
import ast
import inspect
import unittest
from exercise import flatten


class TestFlattenNestedList(unittest.TestCase):

    def test_standard_nesting(self):
        self.assertEqual(flatten([1, [2, [3, 4], 5], 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(flatten([[1, 2], [3, [4, [5]]]]), [1, 2, 3, 4, 5])

    def test_already_flat(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])

    def test_empty_variations(self):
        self.assertEqual(flatten([]), [])
        self.assertEqual(flatten([[], [[]], [[[]]]]), [])

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            flatten("not a list")
        with self.assertRaises(TypeError):
            flatten(123)

    def test_no_loops(self):
        source = inspect.getsource(flatten)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops are not allowed.")


if __name__ == "__main__":
    unittest.main()
