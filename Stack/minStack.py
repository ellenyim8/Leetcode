# 155) min stack 

class MinStack:
    
    min = float('inf')
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if val <= self.min:
            self.stack.append(self.min)
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        top = self.stack[-1]
        self.stack.pop()
        if self.min == top:
            self.min = self.stack[-1]
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
    
