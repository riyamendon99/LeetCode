from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        sortedList = SortedList()
        left = 0
        right = 0
        result = []
        neg_count = 0
        while right<len(nums):
            sortedList.add(nums[right])
            if nums[right]<0:
                neg_count = neg_count + 1
            if right-left+1 == k:
                if neg_count >= x:
                    result.append(sortedList[x-1])
                else:
                    result.append(0)
                if nums[left]<0:
                    neg_count = neg_count -1
                sortedList.remove(nums[left])
                left = left + 1
            right = right + 1
        return result
        
    #previous attempts
    #I used heap but ran into time limit exception. So I looked up another approach to use sorted list. below is also correct but slow.
    """"  import heapq
    class Solution:
        def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
            left = 0
            right = 0
            result = []
            neg_count = 0
            while right<len(nums):
                if nums[right]<0:
                    neg_count = neg_count + 1
                if right-left+1 == k:
                    if neg_count >= x:
                        subarray = nums[left:right+1]
                        heapq.heapify(subarray)
                        for m in range(0, x):
                            ele = heappop(subarray)
                        result.append(ele)
                    else:
                        result.append(0)
                    if nums[left]<0:
                        neg_count = neg_count -1
                    left = left + 1
                right = right + 1
            return result"""