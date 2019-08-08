"""Tests for Money, Money, Money."""
import pytest


def test_01():
    """First test."""
    from cw03_money import calculate_years
    assert calculate_years(1000, 0.05, 0.18, 1100) == 3


def test_02():
    """Second test."""
    from cw03_money import calculate_years
    assert calculate_years(1000, 0.01625, 0.18, 1200) == 14


def test_03():
    """Third test."""
    from cw03_money import calculate_years
    assert calculate_years(1000, 0.05, 0.18, 1000) == 0


def test_04():
    """Fourth test."""
    from cw03_money import calculate_years
    assert calculate_years(1000, .1, .12, 1100) == 2


def test_05():
    """Fifth test."""
    from cw03_money import calculate_years
    assert calculate_years(2000, .3, .08, 1100) == 0


def test_06():
    """Sixth test."""
    from cw03_money import calculate_years
    assert calculate_years(1000, .01, .22, 1050) == 7


def test_07():
    """Seventh test."""
    from cw03_money import calculate_years
    assert calculate_years(1100, .1, .17, 1300) == 3
