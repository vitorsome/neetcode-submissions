class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_list:
                return [min(i, num_list[diff]), max(i, num_list[diff])]
            num_list[nums[i]] = i