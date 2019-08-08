"""Test for Gau needs help."""

import pytest


def test_01():
    """First test."""
    from cw09_gau import f
    assert f(1) == 1


def test_02():
    """Second test."""
    from cw09_gau import f
    assert f(100) == 5050


def test_03():
    """Third test."""
    from cw09_gau import f
    assert f(5) == 15


def test_04():
    """Fourth test."""
    from cw09_gau import f
    assert f(7) == 28


def test_05():
    """Fifth test."""
    from cw09_gau import f
    assert f(3) == 6


def test_06():
    """Sixth test."""
    from cw09_gau import f
    assert f(2) == 3
