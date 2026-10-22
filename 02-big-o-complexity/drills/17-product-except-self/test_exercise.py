"""
Unit tests for Drill 17: Product Except Self
"""
import ast
import inspect
import unittest
from exercise import product_except_self


class TestProductExceptSelf(unittest.TestCase):

    def test_standard_products(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_no_division_used(self):
        source = inspect.getsource(product_except_self)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Div, ast.FloorDiv)):
                self.fail("Division is strictly forbidden!")


if __name__ == "__main__":
    unittest.main()
