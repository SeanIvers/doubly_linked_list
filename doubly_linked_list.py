# Doubly Linked List Data Structure

class DLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    