"""
Solution for Drill 06: Recursive Palindrome Check
Module: 01-recursion
"""


def is_palindrome(text: str, left: int = 0, right: int | None = None) -> bool:
    """
    Recursively checks if text is a palindrome by comparing text[left] and text[right].
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Initialize right pointer on the first call
    if right is None:
        right = len(text) - 1

    # Base case: if pointers have met or crossed, all pairs matched
    if left >= right:
        return True

    # If current characters do not match, it cannot be a palindrome
    if text[left] != text[right]:
        return False

    # Recursive step: step inward from both sides
    return is_palindrome(text, left + 1, right - 1)
