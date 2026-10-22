"""
Unit tests for Drill 20: 2D Grid Maze Pathfinder
"""
import unittest
from exercise import has_path


class TestMazePathfinder(unittest.TestCase):

    def test_open_path(self):
        grid = [
            [0, 0, 1],
            [1, 0, 1],
            [1, 0, 0]
        ]
        self.assertTrue(has_path(grid, (0, 0), (2, 2)))

    def test_blocked_path(self):
        grid = [
            [0, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        self.assertFalse(has_path(grid, (0, 0), (2, 2)))

    def test_start_is_end(self):
        grid = [[0]]
        self.assertTrue(has_path(grid, (0, 0), (0, 0)))

    def test_start_or_end_on_wall(self):
        grid = [[1, 0], [0, 0]]
        self.assertFalse(has_path(grid, (0, 0), (1, 1)))


if __name__ == "__main__":
    unittest.main()
