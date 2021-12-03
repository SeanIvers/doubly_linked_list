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
        new_node = DLNode(val)
        if self.head == None:
            self.head = new_node
            return self
        elif self.tail == None:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.tail = self.head.next
            return self
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        return self

    # add a node to the end of the list
    def add_to_back(self, val):
        new_node = DLNode(val)
        if self.head == None:
            self.head = new_node
            return self
        elif self.tail == None:
            self.tail = new_node
            self.tail.previous = self.head
            self.head.next = self.tail
            return self
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        return self

    # print the values
    def print_values(self):
        current_node = self.head
        if self.head != None:
            while current_node != None:
                print(current_node.value)
                current_node = current_node.next
            return self
        return self

    # print the values in reverse
    def print_reverse(self):
        current_node = self.tail
        if self.head != None:
            if self.tail == None:
                print(self.head.value)
                return self
            while current_node != None:
                print(current_node.value)
                current_node = current_node.previous
            return self

    # delete an existing node
    def delete_value(self, val):
        pass

    # insert a node between existing node with given value
    def insert_at_value(self, val):
        pass

    # insert a node at a certain index n
    def insert_at(self, val, n):
        pass

    # make circular
    def make_circular(self):
        self.tail.next = self.head
        self.head.previous = self.tail
        return self

    # remove duplicate values
    def remove_duplicate_values(self):
        pass

    # reverse values in the list
    def reverse_values(self):
        pass

dll = DList()
# dll.add_to_front(3).add_to_front(2).add_to_front(1).add_to_front(0)
# print("\n")
dll.add_to_back(4).add_to_back(5).add_to_back(6).print_values().print_reverse()
