"""
Unit tests for Drill 13: Pascal Triangle Cell
"""
import ast
import inspect
import unittest
from exercise import pascal


class TestPascalTriangle(unittest.TestCase):

    def test_edge_values(self):
        self.assertEqual(pascal(0, 0), 1)
        self.assertEqual(pascal(5, 0), 1)
        self.assertEqual(pascal(5, 5), 1)

    def test_interior_cells(self):
        # Row 4: 1, 4, 6, 4, 1
        self.assertEqual(pascal(4, 1), 4)
        self.assertEqual(pascal(4, 2), 6)
        self.assertEqual(pascal(4, 3), 4)

    def test_out_of_bounds(self):
        self.assertEqual(pascal(4, -1), 0)
        self.assertEqual(pascal(4, 5), 0)

    def test_large_cell_performance(self):
        # Requires memoization
        self.assertEqual(pascal(30, 15), 155117520)

    def test_no_loops(self):
        source = inspect.getsource(pascal)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops forbidden.")


if __name__ == "__main__":
    unittest.main()
