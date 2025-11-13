class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """I suggested O(n2) solution and a O(n) with extra space. But question wants constant space. REMEMBER!!!!! VVVVIMP !!!! Whenever you see that the question has given us a sorted array. It is a KEYWORD for BINARY SEARCH !!!!!!!!.  ALSO, often times when the question wants a specific time complexity, we can then think of algorithms in those lines. For example we need complexity O(long) we can think of using binary search. One solution is parsing each element and subtracting the target and then doing binary search on the rest of the array to find if that number exists or not. Complexity is O(nlogn). Better solution which is 2 pointer and I SAW HINT For IT !!!!!! Why Riya Why? Should have done on your own. But okay now REMEMBER IT. I will never forget this solution from now on. Since array is sorted, we can have 2 pointers left at index 0 and right at last index. Sum the values of the array at these indexes and check if sum is greater than target then decrement right pointer and if less than target then increment right pointer."""
        left = 0
        right = len(numbers)-1

        while (numbers[left] + numbers[right] != target):
            numberSum = numbers[left] + numbers[right]
            if (numberSum > target):
                right -= 1
            else:
                left += 1

        result = []
        result.append(left+1)
        result.append(right+1)
        return result
