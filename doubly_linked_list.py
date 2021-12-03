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
        elif self.tail == None: # case of only self.head no self.tail node
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
            self.tail = new_node.next
            return self
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    # add a node to the end of the list
    def add_to_back(self, val):
        pass

    # print the values
    def print_values(self):
        if self.head != None:
            node = self.head
            if node.next == None:
                print(node.value)
                return self
            while node != None:
                print(node.value)
                node = node.next
            return self
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

    # test if circular linked list
    def is_circular(self):
        if self.tail.next == self.head:
            return True
        return False

    # remove duplicate values
    def remove_duplicate_values(self):
        pass

    # reverse values in the list
    def reverse_values(self):
        pass

dll = DList()
dll.add_to_front(3).add_to_front(2).add_to_front(1).print_values()
print(dll.head.value, dll.tail.value)