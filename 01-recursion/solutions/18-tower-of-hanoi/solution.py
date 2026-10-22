"""
Solution for Drill 18: Tower of Hanoi
Module: 01-recursion
"""


def hanoi(n: int, source: str = "A", target: str = "C", auxiliary: str = "B") -> list[tuple[str, str]]:
    """
    Recursively generates optimal sequence of moves.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return []

    moves = []
    # Step 1: Move n - 1 disks from source to auxiliary
    moves.extend(hanoi(n - 1, source, auxiliary, target))
    # Step 2: Move the largest disk directly to target
    moves.append((source, target))
    # Step 3: Move n - 1 disks from auxiliary to target
    moves.extend(hanoi(n - 1, auxiliary, target, source))

    return moves
