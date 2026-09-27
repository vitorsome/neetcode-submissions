class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seen = {};
        let diff = 0;
        for (let i = 0; i < nums.length; i++) {
            diff = target - nums[i];
            if (seen[diff] !== undefined) {
                return [seen[diff], i];
            }
            seen[nums[i]] = i;
        }
    }
}
