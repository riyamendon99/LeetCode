class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2]
        #hashSet = set(nums)
        result = set()
        
        nums.sort()
        for i in range(0,len(nums)):
            solution_set = set()
            for j in range(i+1, len(nums)):
                numNegate = -(nums[i])
                numRemaining = numNegate - nums[j]
                if numRemaining in solution_set:
                    result.add((nums[i], nums[j], numRemaining))
                #solution_set.add(nums[i])
                solution_set.add(nums[j])
                #solution_set.add(numRemaining)
                    #break
            
        result = list(result)
        return result

        