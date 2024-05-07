class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        result = 0
        for p in range(0, len(piles)):
            heappush(heap, -1*piles[p])
            
        #print("Heap is ", heap)
        
        for i in range(0, k):
            ele = -1*heappop(heap)
            #print("ele popped is ", ele)
            
            heappush(heap, -1*ceil(ele/2))
            #print("Heap now is ", heap)
        
        while heap:
            result = result + (-1*heappop(heap))
        return result
            
        