"""Test for Get the Middle Character"""
import pytest

def test_01():
    from cw05_gtmc import get_middle
    assert get_middle("test") == "es"

def test_02():
    from cw05_gtmc import get_middle
    assert get_middle("testing") == "t"

def test_03():
    from cw05_gtmc import get_middle
    assert get_middle("middle") == "dd"

def test_04():
    from cw05_gtmc import get_middle
    assert get_middle("A") == "A"

def test_05():
    from cw05_gtmc import get_middle
    assert get_middle("of") == "of"

def test_06():
    from cw05_gtmc import get_middle
    assert get_middle("test") == "es"

def test_07():
    from cw05_gtmc import get_middle
    assert get_middle("test") == "es"

def test_08():
    from cw05_gtmc import get_middle
    assert get_middle("test") == "es"

def test_09():
    from cw05_gtmc import get_middle
    assert get_middle("test") == "es"
