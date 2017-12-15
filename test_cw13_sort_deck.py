"""Test for the queue."""


import pytest



def test_empty_queue_does_not_have_head():
    """An empty queue does not have a head."""
    from cw13_sort_deck import Priority_Q
    q = Priority_Q()
    assert q.head is None


def test_empty_queue_does_not_have_tail():
    """An empty queue does not have a tail."""
    from cw13_sort_deck import Priority_Q
    q = Priority_Q()
    assert q.tail is None


def test_insert_creates_head():
    """Inserting a node will create a head."""
    from cw13_sort_deck import Priority_Q
    q = Priority_Q()
    q.insert('T')
    q.insert('A')
    assert q.head.data is 'A'


