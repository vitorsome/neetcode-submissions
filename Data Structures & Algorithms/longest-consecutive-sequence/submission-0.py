class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapp = set(nums)
        long_seq = 0

        for num in mapp:
            if num - 1 not in mapp:
                current = num
                seq = 1
                while current + 1 in mapp:
                    current += 1
                    seq += 1
                long_seq = max(seq, long_seq)
        return long_seq