"""Small statistics helpers."""


def total(numbers: list[int | float] | tuple[int | float, ...]) -> int | float:
    """Return the sum of a list or tuple of int/float values, rejecting anything else."""
    if not isinstance(numbers, (list, tuple)):
        raise TypeError(f"total() expects a list or tuple, got {type(numbers).__name__}")
    for n in numbers:
        if isinstance(n, bool) or not isinstance(n, (int, float)):
            raise TypeError(f"total() expects int or float items, got {type(n).__name__}")
    return sum(numbers)
