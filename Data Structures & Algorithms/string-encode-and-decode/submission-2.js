class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = '';
        for (const str of strs) {
            encoded += str.length+'#'+str;
        }
        return encoded;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let stringLength = 0;
        const decoded = [];
        let j = 0;
        for (let i = 0; i < str.length; i++) {
            if (str[i] === '#') {
                let word = '';
                for (j = i+1; word.length < parseInt(stringLength); j++) {
                    word += str[j];
                    i++;
                }
                decoded.push(word);
                stringLength = 0;
                continue;
            }
            stringLength += str[i];
        }
        return decoded;
    }
}
