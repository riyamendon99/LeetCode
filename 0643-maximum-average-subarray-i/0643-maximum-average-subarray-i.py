class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #optimized version
        left = 0
        right = 0
        sum = 0
        avg = -sys.maxsize
        while right <len(nums):
            sum = sum + nums[right]
            if right - left == k-1:
                avg = max(avg, sum/k)
                sum = sum - nums[left]
                left = left + 1
            right = right + 1
        return round(avg,5)

        #previous
        """left = 0
        avg = -sys.maxsize
        right = 0
        while right<len(nums):
            right = left
            sum = 0
            while right-left < k:
                sum = sum + nums[right]
                right += 1
            avg = max(avg, sum/k)
            left += 1
        return round(avg,5)"""
        