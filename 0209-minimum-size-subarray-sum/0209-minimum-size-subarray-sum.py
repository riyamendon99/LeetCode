class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        length = len(nums) + 1
        sum_terms = 0
        while right<len(nums):
            sum_terms = sum_terms + nums[right]
            while left<=right and sum_terms>=target:
                length = min(length, right-left + 1)
                sum_terms =  sum_terms - nums[left]
                left = left + 1
            right = right + 1
        if length == len(nums) + 1:
            return 0
        return length

        #Previous Version:
        #Very repetitive and not clean
        left = 0
        right = 0
        length = len(nums) + 1
        sum_terms = 0
        while right<len(nums):
            sum_terms = sum_terms + nums[right]
            if sum_terms >= target:
                length = min(length, right-left + 1)
                while left<=right and sum_terms>=target:
                    sum_terms =  sum_terms - nums[left]
                    left = left + 1
                    if sum_terms>=target:
                        length = min(length, right-left + 1)
            right = right + 1
        if length == len(nums) + 1:
            return 0
        return length