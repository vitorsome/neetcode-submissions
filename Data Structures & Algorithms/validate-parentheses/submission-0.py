class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        endings = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for c in s:
            if c in endings:
                if len(stack) > 0 and stack[-1] == endings[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0


        
        