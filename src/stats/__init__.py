"""Small statistics helpers."""

from collections.abc import Sequence


def total(numbers: list[int | float] | tuple[int | float, ...]) -> int | float:
    """Return the sum of a list or tuple of int/float values, rejecting anything else."""
    if not isinstance(numbers, (list, tuple)):
        raise TypeError(f"total() expects a list or tuple, got {type(numbers).__name__}")
    for n in numbers:
        if isinstance(n, bool) or not isinstance(n, (int, float)):
            raise TypeError(f"total() expects int or float items, got {type(n).__name__}")
    return sum(numbers)


def mean(numbers: Sequence[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers."""
    if not numbers:
        raise ValueError("mean() requires at least one number")
    return sum(numbers) / len(numbers)
