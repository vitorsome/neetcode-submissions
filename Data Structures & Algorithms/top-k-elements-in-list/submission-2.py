import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        
        heap = []
        for key, value in frequency.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        top_k = []
        for i in range(len(heap)):
            top_k.append(heapq.heappop(heap)[1])
        
        return top_k