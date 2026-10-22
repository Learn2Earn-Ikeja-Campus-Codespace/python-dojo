"""
Unit tests for Drill 18: Tower of Hanoi
"""
import ast
import inspect
import unittest
from exercise import hanoi


class TestTowerOfHanoi(unittest.TestCase):

    def test_single_disk(self):
        self.assertEqual(hanoi(1, "A", "C", "B"), [("A", "C")])

    def test_two_disks(self):
        moves = hanoi(2, "A", "C", "B")
        self.assertEqual(len(moves), 3) # 2^2 - 1
        self.assertEqual(moves, [("A", "B"), ("A", "C"), ("B", "C")])

    def test_three_disks(self):
        moves = hanoi(3, "A", "C", "B")
        self.assertEqual(len(moves), 7) # 2^3 - 1

    def test_zero_disks(self):
        self.assertEqual(hanoi(0), [])

    def test_negative_disks(self):
        with self.assertRaises(ValueError):
            hanoi(-1)

    def test_no_loops(self):
        source = inspect.getsource(hanoi)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops forbidden.")


if __name__ == "__main__":
    unittest.main()
