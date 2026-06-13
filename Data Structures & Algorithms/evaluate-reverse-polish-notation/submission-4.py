class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']
        for char in tokens:
            if char in operands:
                n2 = stack.pop()
                n1 = stack.pop()
                result = int(eval(str(n1) + char + str(n2)))
                stack.append(result)
            else:
                stack.append(char)
        return int(stack[-1])