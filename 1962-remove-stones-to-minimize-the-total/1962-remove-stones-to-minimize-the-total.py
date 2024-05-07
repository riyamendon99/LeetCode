class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """Learn basic heap functionalities- How to form a max heap, heappush, heappop, ceil"""
        
        heap = []
        heapq.heapify(heap)
        result = 0
        for p in range(0, len(piles)):
            heappush(heap, -1*piles[p])
        
        for i in range(0, k):
            ele = -1*heappop(heap)
            heappush(heap, -1*ceil(ele/2))
        
        while heap:
            result = result + (-1*heappop(heap))
        return result
            
        