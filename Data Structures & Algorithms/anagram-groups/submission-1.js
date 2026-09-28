class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const groups = {};
        for (const word of strs) {
            const groupIndexArray = Array(26).fill(0);
            for (const char of word) {
                const index = char.charCodeAt(0) - 'a'.charCodeAt(0);
                groupIndexArray[index]++;
            }
            const groupIndex = groupIndexArray.join(',');
            if (typeof groups[groupIndex] === 'undefined') {
                groups[groupIndex] = [word];
            } else {
                groups[groupIndex].push(word);
            }
        }
        return Object.values(groups);
    }
}
