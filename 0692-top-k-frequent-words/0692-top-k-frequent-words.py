class HeapItem:
    def __init__(self, word: str, count: int) ->None:
        self.word = word
        self.count = count
    def __lt__(self, to_compare) -> bool:
        if self.count == to_compare.count:
            return self.word>to_compare.word
        return self.count < to_compare.count






class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #We need to create a custom heap
        
        word_counts = collections.Counter(words)
        heap = []
        for word, count in word_counts.items():
            item = HeapItem(word, count)
            if len(heap) < k:
                heappush(heap, item)
            else:
                if item > heap[0]:
                    heappop(heap)
                    heappush(heap, item)
        result = []
        
        while k:
            ele = heappop(heap)
            result.append(ele.word)
            k -= 1
        return reversed(result)
        """hashMap = {}
        for w in words:
            if w not in hashMap:
                hashMap[w] = 1
            else:
                hashMap[w] += 1
    
        heap = []
        for key in hashMap:
            heappush(heap, (hashMap[key],key))
        sortedList = heapq.nlargest(k, heap)
        
        sortedList = sorted(sortedList, key=lambda i: (i[0], i[1]), reverse=True)
        
        print(sortedList)
        result = []
        for x,y in sortedList:
            result.append(y)
        
        return result"""
        