class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let right = s.length - 1;
        let left = 0;
        while (left < right) {
            if (!/^[a-zA-Z0-9]+$/.test(s[left])) {
                left++;
                continue;
            }
            if (!/^[a-zA-Z0-9]+$/.test(s[right])) {
                right--;
                continue;
            }
            if (s[left].toUpperCase() !== s[right].toUpperCase()) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
