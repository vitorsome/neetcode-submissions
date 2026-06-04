class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_val = 0
        l = 0
        n = len(heights)
        r = n - 1
        while l < r:
            min_wall = min(heights[l], heights[r])
            width = r - l
            curr_val = min_wall * width
            max_val = max(max_val, curr_val)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_val

        
        