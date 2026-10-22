"""
Unit tests for Drill 10: Deep Nested Dictionary Lookup
"""
import ast
import inspect
import unittest
from exercise import deep_get


class TestNestedDictLookup(unittest.TestCase):

    def setUp(self):
        self.data = {
            "a": {
                "b": {
                    "c": 42
                },
                "list_val": 99
            }
        }

    def test_successful_lookup(self):
        self.assertEqual(deep_get(self.data, ["a", "b", "c"]), 42)
        self.assertEqual(deep_get(self.data, ["a", "list_val"]), 99)

    def test_missing_keys(self):
        self.assertIsNone(deep_get(self.data, ["a", "nonexistent"]))
        self.assertIsNone(deep_get(self.data, ["z", "b", "c"]))
        self.assertIsNone(deep_get(self.data, []))

    def test_traversing_into_non_dict(self):
        # Trying to traverse into 42 as if it were a dict
        self.assertIsNone(deep_get(self.data, ["a", "b", "c", "d"]))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            deep_get("not a dict", ["a"])

    def test_no_loops(self):
        source = inspect.getsource(deep_get)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops are not allowed.")


if __name__ == "__main__":
    unittest.main()
