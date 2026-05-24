class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in num_map:
                return [num_map[diff], i]
            num_map[nums[i]] = i
        