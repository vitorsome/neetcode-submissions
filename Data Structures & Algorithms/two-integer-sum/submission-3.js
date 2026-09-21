class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const nums_checked = {}
        let diff;
        for (let i = 0; i < nums.length; i++) {
            diff = target - nums[i];
            if (nums_checked[diff] !== undefined) {
                return [nums_checked[diff], i];
            }  
            nums_checked[nums[i]] = i;
        }
    }
}
