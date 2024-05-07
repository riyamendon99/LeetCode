class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """Learn basic heap functionalities- How to form a max heap, heappush, heappop, ceil"""
        
        """Below is 2 liner code. learn from this and use this in next questions---->

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles_neg = [-a for a in piles]
        heapq.heapify(piles_neg)

        for _ in range(k):
            cur = heapq.heappop(piles_neg) // 2
            heapq.heappush(piles_neg, cur)
        
        return -sum(piles_neg)"""
        
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
            
        