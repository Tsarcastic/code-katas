"""Test the New Member Module"""

import pytest

def test_01():
    from cw06_new_member import openOrSenior
    assert openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]) == ['Open', 'Senior', 'Open', 'Senior']

def test_02():
    from cw06_new_member import openOrSenior
    assert openOrSenior([[16, 23],[73,1],[56, 20],[1, -1]]) == ['Open', 'Open', 'Senior', 'Open']

def test_03():
    from cw06_new_member import openOrSenior
    assert openOrSenior([[16, 23],[12,1],[19, 20],[1, -1]]) == ['Open', 'Open', 'Open', 'Open']

def test_04():
    from cw06_new_member import openOrSenior
    assert openOrSenior([[60, 23],[73,10],[56, 20],[60, 23]]) == ['Senior', 'Senior', 'Senior', 'Senior']

def test_05():
    from cw06_new_member import openOrSenior
    assert openOrSenior([[70, 23],[73,1],[56, 15],[88, -1]]) == ['Senior', 'Open', 'Senior', 'Open']

def test_06():
    from cw06_new_member import openOrSenior
    assert openOrSenior([[16, 23],[73,1],[72, 9],[1, -1]]) == ['Open', 'Open', 'Senior', 'Open']