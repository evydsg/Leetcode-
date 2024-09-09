import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-element for element in nums]
        heapq.heapify(max_heap)

        for element in range(k-1):
            heapq.heappop(max_heap)

        return -heapq.heappop(max_heap)
        