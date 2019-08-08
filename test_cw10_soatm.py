"""Test for 'Sum of all the multiples of 3 or 5."""

import pytest


def test_01():
    """First test."""
    from cw10_soatm import find
    assert find(5) == 8


def test_02():
    """Second test."""
    from cw10_soatm import find
    assert find(10) == 33


def test_03():
    """Third test."""
    from cw10_soatm import find
    assert find(4) == 3


def test_04():
    """Fourth test."""
    from cw10_soatm import find
    assert find(12) == 45


def test_05():
    """Fifth test."""
    from cw10_soatm import find
    assert find(18) == 78


def test_06():
    """Sixth test."""
    from cw10_soatm import find
    assert find(10) == 33


def test_07():
    """Seventh test."""
    from cw10_soatm import find
    assert find(1) == 0
