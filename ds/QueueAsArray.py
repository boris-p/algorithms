# fifo queue implemented as array
class QueueAsArr:
    def __init__(self):
      self.queueList = []
    def push(self, value):
      self.queueList.insert(0,value)
    def pop(self):
      listLength = len(self.queueList)
      if listLength == 0:
        print("queue empty")
        return None
      else:
        item = self.queueList[listLength -1]
        del self.queueList[listLength -1]
        print(item)
        return item

ll = QueueAsArr()

ll.push("first in line")
ll.push("second in line")
ll.push("third in line")
ll.pop()
ll.pop()
ll.pop()
ll.pop()


