import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i] * -1)

        kth = None
        for _ in range(k):
            kth = heapq.heappop(heap) * -1
        
        return kth


        