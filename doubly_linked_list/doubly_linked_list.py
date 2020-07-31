"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # If list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
       
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
   def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # first node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)


      def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev   

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # the list is empty
        if  self.head  is None and not self.tail is None:
            return
        # the list is only one node
        self.length -= 1
        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
        # if deleting head
        # get the next node reference from node being deleted
        # change head reference to next node
        # delete node
        elif self.head is node:
            self.head = node.next
            node.delete()
        # if deleting tail
        # get the prev node reference from node being deleted
        # change tail reference to prev node
        # delete node
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        # no node case
        # -?
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # start at head
        current = self.head
        # get value
        max_value = current.value
        # iterate through the nodes via their next reference
        # compare max and current, keep track of max
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
© 2020 GitHub, Inc.