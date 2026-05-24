class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}
        n = len(strs)
        for i in range(n):
            sorted_string = "".join(sorted(strs[i]))
            if sorted_string not in freq_map:
                freq_map[sorted_string] = []
            freq_map[sorted_string].append(strs[i])

        return list(freq_map.values())



        