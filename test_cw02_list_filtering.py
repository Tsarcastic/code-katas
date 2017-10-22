"""Tests for List Filtering Code Kata"""
import pytest

def test_01():
    from cw02_list_filtering import filter_list
    assert filter_list([1, 2, 'a', 'b']) == [1, 2]

def test_02():
    from cw02_list_filtering import filter_list
    assert filter_list([1, 'a', 'b', 0,15]) == [1, 0, 15]

def test_03():
    from cw02_list_filtering import filter_list
    assert filter_list([1, 2,'aasf', '1', '123', 123]) == [1, 2, 123]

def test_04():
    from cw02_list_filtering import filter_list
    assert filter_list([2, 'iamtheverymodel']) == [2]

def test_05():
    from cw02_list_filtering import filter_list
    assert filter_list(['of', 'a', 15]) == [15]  

def test_06():
    from cw02_list_filtering import filter_list
    assert filter_list(['modern major', 7, 19]) == [7, 19] 

def test_07():
    from cw02_list_filtering import filter_list
    assert filter_list([1, 'a', 'b']) == [1] 
