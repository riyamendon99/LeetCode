class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for t in trips:
            if capacity<t[0]:
                return False
        heap = []
        heap1 = []
        for t in trips:
            heappush(heap,[t[1], t[0]])
            heappush(heap1, [t[2],t[0]])
        km = 0
        total = 0
        while heap:
            while heap1 and km == heap1[0][0]:
                toDes, numPass = heappop(heap1)
                total = total - numPass
            while heap and km == heap[0][0]:
                fromDes, numPass = heappop(heap)
                total = total + numPass
                if capacity<total:
                    return False 
            km += 1
        return True
            
            
            