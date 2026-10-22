"""
Solution for Drill 17: Product Except Self
Module: 02-big-o-complexity
"""


def product_except_self(nums: list[int]) -> list[int]:
    """Computes array of products except self in O(n) time and O(1) auxiliary space without division."""
    n = len(nums)
    res = [1] * n

    # Step 1: Accumulate prefix products
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # Step 2: Multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res
