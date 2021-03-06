"""Test Count of Positives / Sum of Negatives"""

import pytest

def test_01():
    from cw01_count_of_positives_sum_of_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65]


def test_02():
    from cw01_count_of_positives_sum_of_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8,-50]


def test_03():
    from cw01_count_of_positives_sum_of_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([1]) == [1,0]


def test_04():
    from cw01_count_of_positives_sum_of_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([-1]) == [0,-1]


def test_05():
    from cw01_count_of_positives_sum_of_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]) == [0, 0]


def test_06():
    from cw01_count_of_positives_sum_of_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([]) == []

def test_07():
    from cw01_count_of_positives_sum_of_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([1, 1, -2]) == [2, -2]  

def test_08():
    from cw01_count_of_positives_sum_of_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([5, 7, 8, -5]) == [3, -5]  

def test_09():
    from cw01_count_of_positives_sum_of_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([100,-5]) == [1, -5]  

def test_10():
    from cw01_count_of_positives_sum_of_negatives import count_positives_sum_negatives
    assert count_positives_sum_negatives([-5, -2, -3, 1]) == [1, -10]  