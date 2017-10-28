"""Test Write Number in Expanded Form"""

import pytest

def test_01():
    from cw08_write_num import expanded_form
    assert expanded_form(12) == '10 + 2'

def test_02():
    from cw08_write_num import expanded_form
    assert expanded_form(42) == '40 + 2'
    
def test_03():
    from cw08_write_num import expanded_form    
    assert expanded_form(70304) == '70000 + 300 + 4'

def test_04():
    from cw08_write_num import expanded_form    
    assert expanded_form(404) == '400 + 4'

def test_05():
    from cw08_write_num import expanded_form    
    assert expanded_form(79) == '70 + 9'

def test_06():
    from cw08_write_num import expanded_form    
    assert expanded_form(999) == '900 + 90 + 9'