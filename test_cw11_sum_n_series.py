"""Test cw11."""

import pytest


def test_01():
    """First test."""
    from cw11_sum_n_series import series_sum
    assert series_sum(1) == "1.00"


def test_02():
    """Second test."""
    from cw11_sum_n_series import series_sum
    assert series_sum(2) == "1.25"


def test_03():
    """Third test."""
    from cw11_sum_n_series import series_sum
    assert series_sum(3) == "1.39"
