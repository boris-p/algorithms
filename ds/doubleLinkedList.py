class Node:
    def __init__(self, v):
        self.val = v
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
      self.head = None
      self.tail = None
    def append(self, value):
      n = Node(value)
      # first element
      if self.head == None:
        self.head = n
        self.tail = n
      # not first element
      else:
        h = self.tail
        h.next = n
        n.prev = h
        self.tail = n
    def walk(self):
      if self.head == None:
        print ('list empty')
      else:
        h = self.head
        print(h.val)
        while h.next != None:
          h = h.next
          print(h.val)
    def walkBack(self):
      if self.tail == None:
        print ('list empty')
      else:
        h = self.tail
        print(h.val)
        while h.prev != None:
          h = h.prev
          print(h.val)
    def delete(self, value):
      print("hello world1")
    def find(self, value):
      print("hello world1")

ll = LinkedList()

ll.append("element 1")
ll.append("element 2")
ll.append("element 3")
ll.walk()
print('------------')
ll.walkBack()




