class Node:
    def __init__(self, v):
        self.val = v
        self.prev = None

#  stack (lifo) implemented as array
class StackAsArr:
    def __init__(self):
      self.stackArr = []
    def push(self, value):
      self.stackArr.append(value)
    def pop(self):
      itemsLength = len(self.stackArr)
      if itemsLength == 0:
        print("stack empty")
        return None
      else:
        oldTop = self.stackArr[itemsLength-1]
        del self.stackArr[itemsLength-1]
        print(oldTop)
        return oldTop

ll = StackAsArr()

ll.push("first in line")
ll.push("second in line")
ll.push("third in line")
ll.pop()
ll.pop()
ll.pop()
ll.pop()


