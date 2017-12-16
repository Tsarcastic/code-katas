"""Create a Queue consisting of Nodes."""


class Node(object):
    """A Node which contains a value."""

    def __init__(self, data):
        """Create a new Node. Lower priority is better."""
        self.data = data
        self.previous = None
        self.next_node = None
        if self.data is 'A':
            self.priority = 1
        elif self.data is 'T':
            self.priority = 11
        elif self.data is 'J':
            self.priority = 12
        elif self.data is 'Q':
            self.priority = 13
        elif self.data is 'K':
            self.priority = 14
        else:
            int(data)
            self.priority = int(data)


class Priority_Q(object):
    """A Line of Nodes."""

    def __init__(self, iterable=()):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self._counter = 0
        if hasattr(iterable, '__iter__') or isinstance(iterable, str):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Add a node to the tail of the queue."""
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous = self.tail
            self.tail = new_node

        while new_node.previous and new_node.priority < new_node.previous.priority:
            temp = new_node.previous
            if new_node.previous.previous:
                    new_node.previous.previous.next_node = new_node
                    new_node.previous = new_node.previous.previous
            else:
                new_node.previous = None
                self.head = new_node
            if new_node.next_node:
                temp.next_node = new_node.next_node
                temp.next_node.previous = temp
            else:
                self.tail = temp
            new_node.next = temp
            new_node.next.previous = new_node

        self._counter += 1
