"""
Unit tests for Drill 17: Coin Change Combinations Count
"""
import ast
import inspect
import unittest
from exercise import coin_change_ways


class TestCoinChange(unittest.TestCase):

    def test_standard_cases(self):
        self.assertEqual(coin_change_ways(4, [1, 2]), 3)
        self.assertEqual(coin_change_ways(5, [1, 2, 5]), 4)
        self.assertEqual(coin_change_ways(10, [2, 5, 3, 6]), 5)

    def test_impossible_amount(self):
        self.assertEqual(coin_change_ways(3, [2]), 0)

    def test_zero_amount(self):
        self.assertEqual(coin_change_ways(0, [1, 2]), 1)

    def test_large_amount_memoized(self):
        self.assertEqual(coin_change_ways(50, [1, 2, 5, 10, 25]), 292)

    def test_no_loops(self):
        source = inspect.getsource(coin_change_ways)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops forbidden.")


if __name__ == "__main__":
    unittest.main()
