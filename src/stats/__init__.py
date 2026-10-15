"""Small statistics helpers."""

from collections.abc import Sequence


def total(numbers):
    """Return the sum of a list of numbers."""
    return sum(numbers)


def mean(numbers: Sequence[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence of numbers."""
    if not numbers:
        raise ValueError("mean() requires at least one number")
    return sum(numbers) / len(numbers)


def variance(numbers: Sequence[float]) -> float:
    """Return the population variance of a non-empty sequence of numbers."""
    if not numbers:
        raise ValueError("variance() requires at least one number")
    centre = mean(numbers)
    return sum((x - centre) ** 2 for x in numbers) / len(numbers)
