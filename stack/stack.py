from doubly_linked_list import DoublyLinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        #add an elemnt to the front of our aray
        self.size +=1
        self.storage.add_to_tail(value)

    def pop(self):
        #check if empty
        if self.size  == 0:
          return None
        # remove the value from the head of our list
        self.size -= 1
        value = self.storage.remove_from_head()
        return value
