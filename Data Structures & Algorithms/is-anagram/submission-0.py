from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        freq_t = {}
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        for i in range(s_len):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1
        
        return freq_s == freq_t

