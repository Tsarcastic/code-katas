"""Test for Find the Middle Element"""
import pytest

def test_01():
    from cw04_ftme import gimme
    assert gimme([2, 3, 1]) == 0

def test_02():
    from cw04_ftme import gimme
    assert gimme([5, 10, 14]) == 1

def test_03():
    from cw04_ftme import gimme
    assert gimme([99, 17, 50]) == 2
    
def test_02():
    from cw04_ftme import gimme
    assert gimme([5, 72, 14]) == 2

def test_02():
    from cw04_ftme import gimme
    assert gimme([50, 19, 11]) == 1