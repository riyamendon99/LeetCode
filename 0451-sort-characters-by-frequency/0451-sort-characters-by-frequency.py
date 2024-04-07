class Solution:
    def frequencySort(self, s: str) -> str:
        #Discussions Answer
        hashMap = collections.defaultdict(int)
        ans = ''
        heap = []
        heapq.heapify(heap)
        for ele in s:
            hashMap[ele] = hashMap[ele] + 1
        #Adding key,value pairs, sorted based on value in heap    
        for key, value in hashMap.items():
            heapq.heappush(heap, (value, key))
        
        #Converting min heap to maxheap
        result = heapq.nlargest(len(heap), heap)
        
        #Forming the answer string (Yes we can do char*freq)
        for freq, char in result:
            ans = ans + char*freq
        return ans
        
        """hashMap = collections.defaultdict(int)
        for ele in s:
            hashMap[ele] = hashMap[ele] + 1
        arr = list(hashMap.values())
        for j in range(0, len(arr)):
            arr[j] = arr[j]*(-1)
        print("Arr ", arr)
        heapq.heapify(arr)
        result = ''
        while arr:
            val = heapq.heappop(arr)
            for i in range(0, hashMap[val]):
                result = result + hashMap[val]
        return result"""
                    