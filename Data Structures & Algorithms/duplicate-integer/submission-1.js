class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const alreadyCheckedNums = new Set();
        for (const num of nums) {
            if (alreadyCheckedNums.has(num)) {
                return true;
            }
            alreadyCheckedNums.add(num);
        }
        return false;
    }
}
