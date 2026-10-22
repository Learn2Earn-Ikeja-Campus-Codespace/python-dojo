"""
Solution for Drill 15: String Permutations
Module: 01-recursion
"""


def permutations(text: str) -> list[str]:
    """
    Recursively generates all permutations of a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if len(text) <= 1:
        return [text]

    result = []
    for i in range(len(text)):
        char = text[i]
        remaining = text[:i] + text[i+1:]
        for p in permutations(remaining):
            result.append(char + p)

    return result
