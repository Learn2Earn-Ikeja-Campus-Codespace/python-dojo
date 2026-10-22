"""
Unit tests for Drill 11: Fast Exponentiation
"""
import ast
import inspect
import unittest
from exercise import power


class TestFastExponentiation(unittest.TestCase):

    def test_positive_exponents(self):
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(3, 3), 27)
        self.assertEqual(power(5, 4), 625)

    def test_zero_exponent(self):
        self.assertEqual(power(100, 0), 1)
        self.assertEqual(power(-5, 0), 1)

    def test_negative_exponents(self):
        self.assertAlmostEqual(power(2, -2), 0.25)
        self.assertAlmostEqual(power(4, -1), 0.25)

    def test_zero_base(self):
        self.assertEqual(power(0, 5), 0)
        with self.assertRaises(ZeroDivisionError):
            power(0, -2)

    def test_no_shortcuts(self):
        source = inspect.getsource(power)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops forbidden.")
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
                self.fail("** operator is forbidden. Use recursive multiplication.")


if __name__ == "__main__":
    unittest.main()
