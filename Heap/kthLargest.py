# 215) Kth largest element in an array
from collections import List 
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for ele in nums:
            heapq.heappush(heap, ele)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)

        # Time: O(N + (N + k - 1) log (N + k - 1))


