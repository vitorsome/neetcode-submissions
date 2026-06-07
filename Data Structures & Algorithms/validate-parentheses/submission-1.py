class Solution:
    def isValid(self, s: str) -> bool:
        begins = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        n = len(s)
        stack = []
        for char in s:
            if len(stack) > 0 and char in begins:
                if stack[-1] == begins[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0



        
        