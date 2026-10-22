"""
Unit tests for Drill 08: Pure Recursive Binary Search
"""
import ast
import inspect
import unittest
from exercise import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_found_elements(self):
        nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        self.assertEqual(binary_search(nums, 23), 5)
        self.assertEqual(binary_search(nums, 2), 0)
        self.assertEqual(binary_search(nums, 91), 9)

    def test_not_found(self):
        nums = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(nums, 4), -1)
        self.assertEqual(binary_search(nums, -10), -1)
        self.assertEqual(binary_search(nums, 100), -1)

    def test_empty_and_single_element(self):
        self.assertEqual(binary_search([], 5), -1)
        self.assertEqual(binary_search([42], 42), 0)
        self.assertEqual(binary_search([42], 99), -1)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            binary_search("123", 1)
        with self.assertRaises(TypeError):
            binary_search([1, 2], "2")
        with self.assertRaises(TypeError):
            binary_search([1, 2], True)

    def test_no_loops_or_slicing(self):
        source = inspect.getsource(binary_search)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops are not allowed.")
            if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
                self.fail("Slicing creates O(n) memory copies. Use pointers.")


if __name__ == "__main__":
    unittest.main()
