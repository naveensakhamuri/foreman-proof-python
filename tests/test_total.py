from decimal import Decimal

import pytest

from stats import total


def test_total_adds_numbers():
    assert total([1, 2, 3]) == 6
    assert total([]) == 0


def test_total_accepts_ints_and_floats():
    assert total([1, 2.5]) == 3.5


def test_total_accepts_tuple():
    assert total((1, 2)) == 3
    assert total(()) == 0


def test_total_rejects_string():
    with pytest.raises(TypeError):
        total("12")


@pytest.mark.parametrize(
    "bad",
    [{1, 2}, (x for x in [1]), None, 5],
    ids=["set", "generator", "none", "int"],
)
def test_total_rejects_non_sequence(bad):
    with pytest.raises(TypeError):
        total(bad)


def test_total_rejects_non_number_item():
    with pytest.raises(TypeError):
        total([1, "2"])


def test_total_rejects_bool():
    with pytest.raises(TypeError):
        total([True])
    with pytest.raises(TypeError):
        total([1, False])


def test_total_rejects_other_numeric():
    with pytest.raises(TypeError):
        total([Decimal("1")])
