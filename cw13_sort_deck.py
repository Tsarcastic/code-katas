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
        elif self.data is int:
            self.priority = 2
        elif self.data is 'T':
            self.priority = 3
        elif self.data is 'J':
            self.priority = 4
        elif self.data is 'Q':
            self.priority = 5
        elif self.data is 'K':
            self.priority = 6


class Priority_Q(object):
    """A Line of Nodes."""

    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self._counter = 0

    def insert(self, val, priority=99):
        """Add a node to the tail of the queue."""
        new_node = Node(val, self.tail, priority)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous = self.tail
            self.tail = new_node
        while new_node.priority < new_node.previous.priority:
            new_node.previous

        self._counter += 1