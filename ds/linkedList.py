class Node:
    def __init__(self, v):
        self.val = v
        self.next = None

class LinkedList:
    def __init__(self):
      self.head = None
    def prepend(self, value):
      print("hello world1")
        #n = Node(value)
        #return n
    def append(self, value):
      n = Node(value)
      if self.head == None:
        self.head = n
      else:
        h = self.head
        while h.next != None:
          h = h.next
        h.next = n
    def walk(self):
      if self.head == None:
        print ('list empty')
      else:
        h = self.head
        print(h.val)
        while h.next != None:
          h = h.next
          print(h.val)
    def delete(self, value):
      foundElement = False
      prev = None
      if self.head != None:
        h = self.head
        while h.next != None:
          if h.val == value:
            if prev == None:
              # we're deleting the first element
              self.head = h.next
            else:
              prev.next = h.next
            foundElement = True
            break
          else :
            prev = h
            h = h.next
        # the item we want to delete is the last one
        if foundElement == False and h.val == value:
          foundElement = True
          if prev == None:
            self.head = h.next
          else:
            prev.next = h.next
      return foundElement
    def find(self, value):
      print("hello world1")

ll = LinkedList()

ll.append("element 1")
ll.append("element 2")
ll.append("element 3")
ll.walk()
print ('---------------')
foundElement = ll.delete('element 3')
print ('found element: ' + str(foundElement))
ll.walk()




