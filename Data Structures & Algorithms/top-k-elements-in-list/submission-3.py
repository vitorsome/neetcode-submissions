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
        while heap:
            count, num = heapq.heappop(heap)
            top_k.append(num)
        return top_k