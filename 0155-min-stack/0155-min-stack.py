class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        cur_min = float("inf")
        for i in range(len(self.stack)):
            if self.stack[i] < cur_min:
                cur_min = self.stack[i]
        return cur_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()