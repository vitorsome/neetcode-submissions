import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        for char in tokens:
            if char in operands:
                n2 = stack.pop()
                n1 = stack.pop()
                result = int(operators[char](n1, n2))
                stack.append(result)
            else:
                stack.append(int(char))
        return stack[-1]