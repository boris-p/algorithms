class Node:
    def __init__(self, v):
        self.val = v
        self.prev = None

# fifo queue implemented as linked list
class Queue:
    def __init__(self):
      self.head = None
      self.tail = None
    def push(self, value):
      # first element
      n = Node(value)
      if self.head == None:
        self.head = n
        self.tail = n
      # not first element
      else:
        oldHead = self.head
        oldHead.prev = n
        self.head = n
    def pop(self):
      if self.tail == None:
        print("queue empty")
        return None
      else:
        oldTail = self.tail
        self.tail = oldTail.prev
        print(oldTail.val)
        return oldTail

ll = Queue()

ll.push("first in line")
ll.push("second in line")
ll.push("third in line")
ll.pop()
ll.pop()
ll.pop()
ll.pop()


