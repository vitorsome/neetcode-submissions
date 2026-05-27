class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n
        mult_l = 1
        mult_r = 1

        for i in range(n):
            j = -i -1
            l_arr[i] = mult_l
            r_arr[j] = mult_r
            mult_l *= nums[i]
            mult_r *= nums[j]
            
        
        return [l*r for l, r in zip(l_arr, r_arr)]
