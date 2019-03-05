class Node:
    def __init__(self, v):
        self.val = v
        self.prev = None

#  stack (lifo) implemented as linked list
class Stack:
    def __init__(self):
      self.top = None
    def push(self, value):
      # first element
      n = Node(value)
      if self.top == None:
        self.top = n
      # not first element
      else:
        oldTop = self.top
        n.prev = oldTop
        self.top = n
    def pop(self):
      if self.top == None:
        print("stack empty")
        return None
      else:
        oldTop = self.top
        self.top = oldTop.prev
        print(oldTop.val)
        return oldTop

ll = Stack()

ll.push("first in line")
ll.push("second in line")
ll.push("third in line")
ll.pop()
ll.pop()
ll.pop()
ll.pop()


