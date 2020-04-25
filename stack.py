class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
 
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            neNode = Node(data)
            newNode.next = self.head
            self.head = newNode
    def empty():
        return self.head == None
    def pop(self):
        if self.empty():
            raise NameError("Stack empty")
        else:
            elmt = self.head.data
            self.head = self.head.next
            return elmt
