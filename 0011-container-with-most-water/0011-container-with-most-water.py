class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        maxArea = 0
        while left<right:
            maxHeight = min(height[left], height[right])
            maxArea = max(maxArea, maxHeight*(right-left))
            if(height[left]>height[right]):
                right-=1
            else:
                left +=1
        return maxArea
        