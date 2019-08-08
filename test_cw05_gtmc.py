"""Test for Get the Middle Character."""
import pytest


def test_01():
    """First test."""
    from cw05_gtmc import get_middle
    assert get_middle("test") == "es"


def test_02():
    """Second test."""
    from cw05_gtmc import get_middle
    assert get_middle("testing") == "t"


def test_03():
    """Third test."""
    from cw05_gtmc import get_middle
    assert get_middle("middle") == "dd"


def test_04():
    """Fourth test."""
    from cw05_gtmc import get_middle
    assert get_middle("A") == "A"


def test_05():
    """Fifth test."""
    from cw05_gtmc import get_middle
    assert get_middle("of") == "of"


def test_06():
    """Sixth test."""
    from cw05_gtmc import get_middle
    assert get_middle("test") == "es"


def test_07():
    """Seventh test."""
    from cw05_gtmc import get_middle
    assert get_middle("test") == "es"


def test_08():
    """Eight test."""
    from cw05_gtmc import get_middle
    assert get_middle("test") == "es"


def test_09():
    """Ninth test."""
    from cw05_gtmc import get_middle
    assert get_middle("test") == "es"
