class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        minV = val
        if len(self.stack) > 0:
            minV = self.stack[-1][1]
        self.stack.append((val, min(minV, val)))
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

        
