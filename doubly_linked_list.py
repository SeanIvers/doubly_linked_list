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

    # add node to front of the list
    def add_to_front(self, val):
        pass

    # add a node to the end of the list
    def add_to_back(self, val):
        pass

    # print the values
    def print_values(self):
        pass

    # delete an existing node
    def delete_value(self, val):
        pass

    # insert a node between existing node with given value
    def insert_at_value(self, val):
        pass

    # insert a node at a certain index n
    def insert_at(self, val, n):
        pass

    # test if circular liked list
    def is_circular(self):
        pass

    # remove duplicate values
    def remove_duplicate_values(self):
        pass

    # reverse values in the list
    def reverse_values(self):
        pass