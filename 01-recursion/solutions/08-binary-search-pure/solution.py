"""
Solution for Drill 08: Pure Recursive Binary Search
Module: 01-recursion
"""


def binary_search(arr: list[int], target: int, low: int = 0, high: int | None = None) -> int:
    """
    Recursively searches for target in sorted arr using binary search pointers.
    Time Complexity: O(log n)
    Auxiliary Space: O(log n) call stack
    """
    if not isinstance(arr, list):
        raise TypeError("arr must be a list")
    if isinstance(target, bool) or not isinstance(target, int):
        raise TypeError("target must be an integer")

    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)
