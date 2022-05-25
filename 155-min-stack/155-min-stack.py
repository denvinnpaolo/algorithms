import sys
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        n = self.stack.pop()
        
        if n == self.min:
            self.setMin()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        
        return self.stack[-1]
  

    def getMin(self) -> int:
        return self.min
    
    def setMin(self):
        newMin = float('inf')
        for n in self.stack:
            if n < newMin:
                newMin = n
        self.min = newMin


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()