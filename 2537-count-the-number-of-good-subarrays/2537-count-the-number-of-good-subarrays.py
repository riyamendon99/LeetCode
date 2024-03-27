class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        dict1 = collections.defaultdict(int)
        def addToMap(val):
            dict1[val] = dict1[val] + 1
            return dict1[val]-1
        def removeFromMap(val1):
            dict1[val1] = dict1[val1] - 1
            return dict1[val1]
        left = 0
        right = 0
        result = 0
        count = 0
        while(right<len(nums)):
            if count<k:
                count = count + addToMap(nums[right])
                #print("Val is ", nums[right])
                #print("Count ", count)
            while count>=k:
                result = result + 1 + len(nums)-(right+1)
                #print("Result is ", result)
                #print("Val 1 is ", nums[left])
                count = count - removeFromMap(nums[left])
                #print("Count Here ", count)
                left = left + 1
            right = right + 1
        return result
                    
        