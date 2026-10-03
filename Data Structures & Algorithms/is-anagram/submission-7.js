class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const chars = {};

        for (let i = 0; i < s.length; i++) {
            chars[s[i]] = (chars[s[i]] || 0) + 1; 
        }

        for (let i = 0; i < t.length; i++) {
            if (typeof chars[t[i]] === 'undefined') {
                return false;
            }
            chars[t[i]] += 1;
        }

        for (const counts of Object.values(chars)) {
            if (counts % 2 != 0) {
                return false;
            }
        }

        return true;
    }
}
