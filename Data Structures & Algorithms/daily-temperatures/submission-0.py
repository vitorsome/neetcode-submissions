class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n
        for i in range(n):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                index = stack[-1]
                result[index] = i - index
                stack.pop()
            stack.append(i)
        return result
