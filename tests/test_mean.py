import pytest

from stats import mean


def test_mean_of_integers():
    assert mean([1, 2, 3]) == 2


def test_mean_returns_fractional_result():
    assert mean([1, 2]) == 1.5


def test_mean_of_single_value():
    assert mean([4.0]) == 4.0


def test_mean_accepts_tuple():
    assert mean((2, 4)) == 3


def test_mean_of_empty_raises_value_error():
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        mean(())
