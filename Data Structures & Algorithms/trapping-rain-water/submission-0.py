class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [0] * n
        max_r = [0] * n
        for i in range(n):
            j = -i - 1
            max_l[i] = max(max_l[i - 1], height[i])
            max_r[j] = max(max_r[j + 1], height[j])
        trapped = 0
        for i in range(n):
            curr_trapped = min(max_l[i], max_r[i]) - height[i]
            if curr_trapped < 0:
                curr_trapped = 0
            trapped += curr_trapped
        return trapped




