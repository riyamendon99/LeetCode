class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """heap = []
        hashMap = {}
        
        for letter in tasks:
            if letter not in hashMap:
                hashMap[letter] = 1
            else:
                hashMap[letter] += 1
        
        for ele in hashMap.keys():
            heappush(heap, -hashMap[ele])"""
        
        #Better way to write the above code. There is one inbuilt class in python that acts as a hashMap. USE IT!!!
        count = Counter(tasks) # This does the job of counting all occurances of letters
        heap =[-cnt for cnt in count.values()] # Better way to add values in heap
        heapq.heapify(heap)
        
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                val = 1 + heappop(heap)
                if val:
                    q.append([val, time+n])
            
            #value, t = q[0]
            #if t == time:
            #Better way to write the above commented lines
            if q and q[0][1] == time:
                #value, t = q.popleft()
                heappush(heap, q.popleft()[0])
        return time
            
            
        #My previous code. Was not able to buid the logic.
        """heap = []
        cannotAdd = {}
        result = []
        
        hashMap = {}
        
        for letter in tasks:
            if letter not in hashMap:
                hashMap[letter] = 1
            else:
                hashMap[letter] += 1
        
        for ele in hashMap.keys():
            heappush(heap, (-hashMap[ele], ele))
        
        while hashMap:
            value, l = heappop(heap)
            if l in cannotAdd:
                val, ele = nsmallest(1,heap)
                if ele in cannotAdd:
                    result.append("idle")
                else:
                    cannotAdd[ele] = n
                    result.append(ele)
                    heappush(heap, (val+1,ele))
                heappush(heap,(value,l))
            else:
                cannotAdd[l] = n
                result.append(l)
                heappush(heap, (value+1,l))
        return len(result)"""
                
            
            
        