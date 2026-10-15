import pytest

from stats import variance


def test_variance_of_known_sample():
    assert variance([2, 4, 4, 4, 5, 5, 7, 9]) == 4


def test_variance_is_population_not_sample():
    assert variance([1, 2, 3, 4]) == 1.25


def test_variance_of_single_value_is_zero():
    assert variance([7]) == 0


def test_variance_of_identical_values_is_zero():
    assert variance([3, 3, 3]) == 0


def test_variance_accepts_tuple():
    assert variance((1, 3)) == 1


def test_variance_returns_float():
    result = variance([1, 2])
    assert isinstance(result, float)
    assert result == 0.25


def test_variance_of_empty_raises_value_error():
    with pytest.raises(ValueError, match="variance"):
        variance([])
    with pytest.raises(ValueError, match="variance"):
        variance(())
