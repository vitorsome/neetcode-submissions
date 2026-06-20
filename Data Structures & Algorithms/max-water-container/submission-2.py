class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        max_amount = 0
        while l <= r:
            smallest_bar = min(heights[l], heights[r])
            amount = smallest_bar * (r - l)
            max_amount = max(amount, max_amount)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_amount

