"""Test for Gau needs help!"""

import pytest

def test_01():
    from cw09_gau import f
    assert f(1) == 1

def test_02():
    from cw09_gau import f
    assert f(100) == 5050

def test_03():
    from cw09_gau import f
    assert f(5) == 15

def test_04():
    from cw09_gau import f
    assert f(7) == 28

def test_05():
    from cw09_gau import f
    assert f(3) == 6

def test_01():
    from cw09_gau import f
    assert f(2) == 3