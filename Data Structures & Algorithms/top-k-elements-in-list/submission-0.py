import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i, 0) + 1
        
        max_heap = []
        for key, value in frequency.items():
            heapq.heappush(max_heap, (value * -1, key))
        
        top_k = []
        for i in range(k):
            top_k.append(heapq.heappop(max_heap)[1])
        
        return top_k