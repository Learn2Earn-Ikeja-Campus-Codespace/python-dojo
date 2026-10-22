"""
Unit tests for Drill 06: Prefix Sum Optimization
"""
import unittest
from exercise import RangeSumQuery


class TestPrefixSumOptimization(unittest.TestCase):

    def test_range_queries(self):
        rsq = RangeSumQuery([-2, 0, 3, -5, 2, -1])
        self.assertEqual(rsq.query(0, 2), 1)  # -2 + 0 + 3 = 1
        self.assertEqual(rsq.query(2, 5), -1) # 3 + -5 + 2 + -1 = -1
        self.assertEqual(rsq.query(0, 5), -3)

    def test_single_element_query(self):
        rsq = RangeSumQuery([10, 20, 30])
        self.assertEqual(rsq.query(1, 1), 20)


if __name__ == "__main__":
    unittest.main()
