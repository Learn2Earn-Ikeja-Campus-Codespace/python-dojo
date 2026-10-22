"""
Solution for Drill 03: Recursive String Reversal
Module: 01-recursion
"""


def reverse_string(text: str) -> str:
    """
    Recursively reverses a string by taking the last character
    and prepending it to the reversal of the remaining substring.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Base case: empty or 1-character string is already reversed
    if len(text) <= 1:
        return text

    # Recursive step: last character + reverse of everything before it
    return text[-1] + reverse_string(text[:-1])
