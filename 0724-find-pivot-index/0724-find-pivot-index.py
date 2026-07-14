class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum =[]
        suffixSum = []

        for i in range(len(nums)):
            if(i-1<0):
                sumOfValues = 0
                prefixSum.append(sumOfValues)
            else:
                sumOfValues = sumOfValues + nums[i-1]
                prefixSum.append(sumOfValues)


        for i in range(len(nums)-1,-1,-1):
            if(i+1 == len(nums)):
                sumOfValues = 0
                suffixSum.append(sumOfValues)
            else:
                sumOfValues = sumOfValues + nums[i+1]
                suffixSum.append(sumOfValues)


        suffixSum = list(reversed(suffixSum))
        result = -1
        for i in range(len(prefixSum)):
            if(prefixSum[i] == suffixSum[i]):
                result = i
                break

        return result


        """[1 7 3 6 5 6]
        [0 1 8 11 17 22]
        [27 20 17 11 6 0]"""
        