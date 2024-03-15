class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #A little hard one. Always remember in Sliding Window, look at fixing the size of window by
        #left and right pointer and not window size variable that you are incrementing. Also, in Sliding Window questions
        #there is always a computation that is repeated and you need to not repeat the same computation again and gain which will lead to time limit exceeded.
        #Adjusting left and right pointer automatically sets the window size so no need for a variable for window size and no need for a loop to handle it.
        prod = 1
        left = 0
        result = 0
        for right in range(0, len(nums)):
            prod = prod * nums[right]
            if prod>=k:
                while prod >=k and left<=right:
                    # Below lines are the key to cut the extra computaion
                    prod = prod/nums[left]
                    left = left +1
            result = result + right - left + 1
        return result
    """Previous Attemps
    
    class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        window_size = 1
        i = 0
        j = 0
        result = 0
        while window_size<=len(nums):
            prod = 1
            while (window_size+i-1)<len(nums) and (j-i) < window_size:
                prod = prod * nums[j]
                j += 1
            if (window_size+i-1)>=len(nums):
                i = 0
                j = 0
                window_size += 1
            else:
                i += 1
                j = i
                if prod < k:
                    result += 1
        return result

        
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod = 1
        right = 0
        left = 0
        result = 0
        while left < len(nums):
            right = left
            while right < len(nums):
                prod = prod*nums[right]
                if prod<k:
                    result = result + 1
                right = right + 1
            left = left + 1
            prod = 1
        return result
        
    """