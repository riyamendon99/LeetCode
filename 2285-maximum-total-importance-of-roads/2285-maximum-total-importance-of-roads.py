class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        #With Heap
        total = 0
        heap = []
        edgeCount = [0]*n
        for n1, n2 in roads:
            edgeCount[n1] += 1
            edgeCount[n2] += 1
        
        for index, value in enumerate(edgeCount):
            heappush(heap,(-value, index))
        print(heap)  
        while n:
            v,i = heappop(heap)
            total += (-v)*n
            n -=1
        return total
        
        """
        without heap
        total = 0
        edgeCount = [0]*n
        for n1, n2 in roads:
            edgeCount[n1] += 1
            edgeCount[n2] += 1
            
        edgeCount.sort()
        edgeCount.reverse()
        for index, value in enumerate(edgeCount):
            total = total + n*value
            n -=1
        return total"""
            
        