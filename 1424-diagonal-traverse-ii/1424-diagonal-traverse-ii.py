class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                total = i+j
                if total not in hashMap:
                    hashMap[total] = [nums[i][j]]
                else:
                    arr = hashMap[total]
                    arr.append(nums[i][j])
                    hashMap[total] = arr
                    
        result = []
        for k in hashMap.keys():
            stack1 = hashMap[k]
            while stack1:
                result.append(stack1.pop())
        return result
                    
                
                
                
                
                
        """heap = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                heappush(heap, (i+j,nums[i][j]))
        
        result = []
        var = 0
        q = deque()
        while heap:
            order, ele = heappop(heap)
            if var == order:
                q.append(ele)
            result.append(ele)
        return result"""
        