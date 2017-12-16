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
    q.insert('A')
    assert q.head.data is 'A'

def test_insert_creates_tail():
    """Inserting a node will create a tail."""
    from cw13_sort_deck import Priority_Q
    q = Priority_Q()
    q.insert('A')
    q.insert('K')
    assert q.head.data is 'A'
    assert q.tail.data is 'K'

def test_priority_insert_works01():
    """Priority will move nodes."""
    from cw13_sort_deck import Priority_Q
    q = Priority_Q()
    q.insert('K')
    q.insert('A')
    assert q.head.data is 'A'
    assert q.tail.data is 'K'    

def test_a_longer_set01():
    """A little bigger."""
    from cw13_sort_deck import Priority_Q
    list = ['A','K', 'Q', 'J']
    q = Priority_Q(list)
    assert q.head.data is 'A'
    assert q.head.next_node.data is 'J'
    assert q.tail.data is 'K'

def test_a_longer_set02():
    """An old fashioned how-do-you-do."""
    from cw13_sort_deck import Priority_Q
    list = ['A', 'K', 'Q', '9', '5', '10']
    q = Priority_Q(list)
    assert q.return_list() is ['A', '5', '9', '10', 'Q', 'K']


