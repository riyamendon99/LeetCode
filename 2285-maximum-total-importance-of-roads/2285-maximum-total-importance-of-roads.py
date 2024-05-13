class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        #With Heap
        #Saw video. It was very simple. I could have done it. Just Greedy dekh ke dar gayi. I knew ki number of outgoing edge se we can assign the values accordingly but I did calculation mistake and didnt see ki node 2 se 4 edge jari hai. I calculated it as 2. So got confused. Complex graph mei dimag kam nai karta. Chi. Mai kar sakti thi yeh.
        total = 0
        heap = []
        edgeCount = [0]*n
        for n1, n2 in roads:
            edgeCount[n1] += 1
            edgeCount[n2] += 1
        
        for index, value in enumerate(edgeCount):
            heappush(heap,(-value, index))
        #print(heap)  
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
            
        