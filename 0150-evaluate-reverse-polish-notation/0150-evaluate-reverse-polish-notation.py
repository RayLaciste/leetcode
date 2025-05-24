class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in '*/+-':
                if t == '+':
                    val = (stack.pop()) + (stack.pop())
                    stack.append(val)
                elif t == '-':
                    b = stack.pop()
                    a = stack.pop()
                    val = int(a-b)
                    stack.append(val)
                elif t == '*':
                    val = (stack.pop()) * (stack.pop())
                    stack.append(val)
                elif t == '/':
                    b = stack.pop()
                    a = stack.pop()
                    val = int(a / b)
                    stack.append(val)
            else:
                stack.append(int(t))
        return(stack[0])