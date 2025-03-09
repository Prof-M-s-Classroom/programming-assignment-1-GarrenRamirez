from distance import Distance

class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """

    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """

    def __init__(self):
        """Initialize the stack with an empty state."""
        self.size = 0
        self.max_size = 5
        self.front = None
        self.rear = None

    def push(self, distance):
        """Add a new Distance object to the stack, replacing the oldest entry if full."""
        new_node = Node(Distance(distance))

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.rear.next = self.front
        elif self.size < self.max_size:
            self.front.next = new_node
            self.front = new_node
            self.front.next = self.rear
        else:
            self.rear = self.rear.next
            self.front.next = new_node
            new_node.next = self.rear
            self.front = new_node
        if self.size < self.max_size:
            self.size += 1

    def pop(self):
        """Remove the oldest entry from the stack."""
        if self.is_empty():
            return None
        elif self.size == 1:
            old_node = self.rear
            self.rear = None
            self.front = None
            return old_node
        else:
            old_node = self.rear
            self.rear = self.rear.next
            self.front.next = self.rear
            return old_node

    def peek(self):
        """Return the most recent temperature entry without removing it."""
        if self.front is None:
            raise IndexError("Stack is Emtpy!")
        else:
            return self.front

    def print_stack(self):
        """Print all stored readings in order from oldest to newest."""
        if self.is_empty():
            return "Stack is Empty!"
        else:
            current_node = self.rear
            for i in range (self.size):
                print(current_node.data.__str__())
                current_node = current_node.next

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return self.size == 0