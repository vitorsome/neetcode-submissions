class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
       const numsSet = new Set(nums);
       let longestSequence = 0;
       for (let num of numsSet) {
            if (!numsSet.has(num - 1)) {
                let currentNum = num;
                let currentSequence = 1;
                
                while (numsSet.has(currentNum + 1)) {
                    currentNum++;
                    currentSequence++;
                }

                longestSequence = Math.max(longestSequence, currentSequence);
            }
       }

       return longestSequence;
    }
}
