class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        n = len(height)
        max_l = [0] * n
        max_r = [0] * n

        for i in range(n):
            j = -i - 1
            max_l[i] = max(max_l[i - 1], height[i])
            max_r[j] = max(max_r[j + 1], height[j])
        
        for i in range(n):
            val = min(max_l[i], max_r[i]) - height[i]
            if val < 0:
                val = 0
            trapped += val
        return trapped

