class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """Watched Video"""
        heap = []
        result = ""
        heapq.heapify(heap)
        #VVVIMP - Whenever you want to sort using heap and you have characters too witht that number to sort, ALWAYS KEEP THE NUMBER IN THE FIRST PLACE.
        for count, char in [(-a,'a'), (-b,'b'), (-c,'c')]:
            if count!=0:
                heappush(heap, (count, char))

        while heap:
            count, char = heappop(heap)
            #Didn't know we could do this --> result[-1] == result[-2] == char
            if len(result)>1 and result[-1] == result[-2] == char:
                if not heap:
                    break
                count2, char2 = heappop(heap)
                result = result + char2
                count2 += 1
                if count2:
                    heappush(heap, (count2, char2))
            else:
                result = result + char
                count += 1
            if count:
                heappush(heap, (count, char))
        return result
        
        """Logic correct but could not write the code
        heap = []
        heapq.heapify(heap)
        result = ""
        if a !=0:
            heappush(heap, ('a', -1*a))
        if b !=0:
            heappush(heap, ('b', -1*b))
        if c !=0:
            heappush(heap, ('c', -1*c))
            
        while len(heap)>1:
            charList = heapq.nlargest(2, heap)
            for ele,count in charList:
                if count>1:
                    result = result + ele + ele
                    #heappush(heap, (ele, -1*(count-2)))
                else:
                    result = result + ele
        if len(heap)==1:
            ele, count = heappop(heap)
            result = result + ele + ele
        else:
            return result"""
        