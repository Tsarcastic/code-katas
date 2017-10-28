"""Create a Queue consisting of Nodes."""


class Node(object):
    """A Node which contains a value."""

    def __init__(self, data, previous):
        """Create a new Node."""
        self.data = data
        self.previous = previous
        self.next_node = None


class Queue(object):
    """A Line of Nodes."""

    def __init__(self):
        """Create an empty queue."""
        self.head = None
        self.tail = None
        self._counter = 0

    def enqueue(self, val):
        """Add a node to the tail of the queue."""
        new_tail = Node(val, self.tail)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next_node = new_tail
            self.tail = new_tail
        self._counter += 1


    def dequeue(self):
        """Remove a node from the head of the queue."""
        if not self.head:
            raise IndexError("There is nothing to dequeue.")
        output = self.head.data
        self.head.next_node.previous = None
        self.head = self.head.next_node
        self._counter -= 1
        return output


    def size(self):
        """Return the size of the queue."""
        return self._counter

    def __len__(self):
        """Work with len() function to find length of linked list."""
        return self._counter


def paranthetic(parens):
        """Tests a string to see if it's open, balanced, or broken."""
        the_queue = Queue()
        parens = list(parens)
        paren_tracker = 0
        for i in parens:
            the_queue.push(i)
        
        while len(the_queue) > 0:
            while paren_tracker >= 0:
                top = the_queue.dequeue()
                if top = "(":
                    paren_tracker += 1
                if top = ")":
                    paren_tracker -+ 1
        if paren_tracker > 1: 
            return 1
        if paren_tracker < -1:
            return -1
        else:
            return paren_tracker

if __name__ == '__main__':
    print(paranthetic(')))((('))
