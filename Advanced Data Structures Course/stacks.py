class Stack:
   def __init__(self):
      self.stack = []

   def add(self, dataval):
# Use list append method to add element
      if dataval not in self.stack:
         self.stack.append(dataval)
         return True
      else:
         return False
        
# Use list pop method to remove element
   def remove(self):
      if len(self.stack) <= 0:
         return ("No element present in the Stack")
      else:
         return self.stack.pop()

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
AStack.add("Fri")
AStack.add("Sat")
AStack.add("Sun")
print(AStack.remove())
print(AStack.remove())