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
        elif self.head.previous == self.tail: # case where it's circular
            self.tail.next = new_node
            new_node.previous = self.tail
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            return self
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    # add a node to the end of the list
    def add_to_back(self, val):
        new_node = DLNode(val)
        if self.head.previous == self.tail:
            self.tail.next = new_node
            new_node.previous = self.tail
            new_node.next = self.head
            self.head.previous = new_node
            self.tail = new_node
            return self
        elif self.head == None:
            self.add_to_front(val)
            return self
        elif self.tail == None:
            self.head.next = new_node
            new_node.previous = self.head
            self.tail = new_node
            return self
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
        return self

    # print the values
    def print_values(self):
        node = self.head
        if self.head.previous == self.tail:
            while node.next != self.head:
                print(node.value)
                node = node.next
            print(self.tail.value)
            return self
        if self.head != None:
            if node.next == None:
                print(node.value)
                return self
            while node != None:
                print(node.value)
                node = node.next
            return self
        return self

    # delete an existing node
    # def delete_value(self, val):
    #     current_node = self.head
    #     if self.is_circular():
    #         while current_node != self.tail:
    #             if current_node.value == val:
    #                 print(current_node.value)
    #                 current_node.previous.next = current_node.next
    #                 print(current_node.previous.next.value)
    #                 current_node.next.previous = current_node.previous
    #                 print(current_node.next.previous.value)
    #                 return self
    #             current_node = current_node.next
    #         self.tail.previous.next = self.head # if val is self.tail.value and list is circular
    #         self.head.previous = self.tail.previous
    #     if self.head != None:
    #         if self.head.value == val:
    #             if self.is_circular():
    #                 self.head.next.previous = self.tail
    #                 self.tail.next = self.head.next
    #                 self.head = self.head.next
    #                 return self
    #             self.head = self.head.next
    #             return self
    #         if self.tail.value == val:
    #             self.tail.previous.next = None
    #             self.tail = self.tail.previous
    #             return self
    #         while current_node != None:
    #             current_node = current_node.next
    #             if current_node.value == val:
    #                 current_node.previous.next = current_node.next
    #                 current_node.next.previous = current_node.previous
    #                 return self
    #     return self

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

# dll = DList()
dll2 = DList()
# dll.add_to_front(3).add_to_front(2).add_to_front(1).print_values()
# print(dll.head.value, dll.tail.value)
# dll2.add_to_back(0).add_to_back(1).add_to_back(2).add_to_back(3)
dll2.add_to_front(2).add_to_front(1).add_to_front(-1).make_circular().print_values()
# print(dll2.tail.next == dll2.head)
print(dll2.head.value, dll2.tail.value)
dll2.add_to_back(2).print_values()




print(dll2.tail.next == dll2.head, dll2.head.previous == dll2.tail)