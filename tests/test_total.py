from stats import total


def test_total_adds_numbers():
    assert total([1, 2, 3]) == 6
    assert total([]) == 0
