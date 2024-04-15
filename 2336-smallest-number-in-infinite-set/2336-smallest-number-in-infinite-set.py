class SmallestInfiniteSet:

    def __init__(self):
        self.arr = []
        for i in range(1,1001):
            self.arr.append(i)
        heapq.heapify(self.arr)
        

    def popSmallest(self) -> int:
        ele = heapq.heappop(self.arr)
        """No need to do the below it automatically updates the list"""
        #self.arr.remove(ele)
        #print(ele)
        return ele
        
        

    def addBack(self, num: int) -> None:
        if num not in self.arr:
            """No need to do the below it automatically updates the list"""
            #self.arr.append(num)
            heapq.heappush(self.arr, num)
            
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)