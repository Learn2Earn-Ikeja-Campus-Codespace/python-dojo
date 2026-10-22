"""
Unit tests for Drill 16: Climbing Stairs
"""
import ast
import inspect
import unittest
from exercise import count_ways


class TestClimbingStairs(unittest.TestCase):

    def test_small_values(self):
        self.assertEqual(count_ways(0), 1)
        self.assertEqual(count_ways(1), 1)
        self.assertEqual(count_ways(2), 2)
        self.assertEqual(count_ways(3), 4)
        self.assertEqual(count_ways(4), 7)

    def test_negative_steps(self):
        self.assertEqual(count_ways(-1), 0)

    def test_performance_memoization(self):
        self.assertEqual(count_ways(30), 53798080)

    def test_no_loops(self):
        source = inspect.getsource(count_ways)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops forbidden.")


if __name__ == "__main__":
    unittest.main()
