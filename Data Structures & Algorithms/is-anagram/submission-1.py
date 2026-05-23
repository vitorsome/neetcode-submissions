from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        for i in range(s_len):
            freq_s[s[i]] = freq_s.get(s[i], 0) + 1
            freq_s[t[i]] = freq_s.get(t[i], 0) - 1
        
        return all(v == 0 for v in freq_s.values())

