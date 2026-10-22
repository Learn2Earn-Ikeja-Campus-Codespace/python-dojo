"""
Unit tests for Drill 12: Greatest Common Divisor
"""
import ast
import inspect
import unittest
from exercise import gcd


class TestGreatestCommonDivisor(unittest.TestCase):

    def test_standard_pairs(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 25), 25)
        self.assertEqual(gcd(17, 13), 1)

    def test_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(7, 0), 7)
        self.assertEqual(gcd(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(gcd(-48, 18), 6)
        self.assertEqual(gcd(48, -18), 6)
        self.assertEqual(gcd(-48, -18), 6)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            gcd(3.5, 2)
        with self.assertRaises(TypeError):
            gcd(4, True)

    def test_no_loops_or_math(self):
        source = inspect.getsource(gcd)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops forbidden.")
            if isinstance(node, ast.Attribute) and node.attr == "gcd":
                self.fail("math.gcd is forbidden.")


if __name__ == "__main__":
    unittest.main()
