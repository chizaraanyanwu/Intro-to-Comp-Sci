"""Starter code for the pytest worksheet."""

from underperformers import collect_underperformers


def test_underperformers_low_threshold():
    """Test collect_underperformers with a threshold for which there are
    no underperformers.

    """

    actual = collect_underperformers([4, 5, 6], 1)
    expected = []
    assert actual == expected


def test_underperformers_high_threshold():
    """Test collect_underperformers with a threshold for which all items
    are underperformers.

    """
    actual = collect_underperformers([4, 5, 6], 3)
    expected = []
    assert actual == expected


def test_underperformers_mutation():
    """Confirm that collect_underperformers does not mutate the input
    list.

    """
    
    expected = [2, 3, 4]
    checker = expected
    original = collect_underperformers(expected, 5)
    assert checker == expected


