from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        def checkLimit(arr):
            if len(arr) == 1:
                return True
            ele = arr[len(arr)-1]
            if abs(ele-arr[0])>limit:
                    return False   
            return True
                
        left = 0
        right = 0
        count = 0
        sl = SortedList()
        while(right<len(nums)):
            sl.add(nums[right])
            while checkLimit(sl) == False:
                sl.remove(nums[left])
                left = left + 1
            count = max(count, right-left+1)
            right = right + 1
        return count
        