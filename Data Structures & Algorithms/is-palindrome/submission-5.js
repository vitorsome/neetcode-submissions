class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let right = s.length - 1;
        let left = 0;
        while (left < right) {
            while (left < right && !/^[a-zA-Z0-9]+$/.test(s[left])) {
                left++;
            }
            while (left < right && !/^[a-zA-Z0-9]+$/.test(s[right])) {
                right--;
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
