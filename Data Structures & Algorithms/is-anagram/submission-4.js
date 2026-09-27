class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const count = {};

        for (const char of s) {
            count[char] = (count[char] || 0) + 1
        }

        for (const char of t) {
            count[char] = (count[char] || 0) - 1
        }

        for (const char of Object.keys(count)) {
            if (count[char] !== 0) {
                return false;
            }
        }
        return true;
    }
}
