class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            else:
                if not stack or c != stack[len(stack) - 1]:
                    return False
                stack.pop()

        return len(stack) == 0