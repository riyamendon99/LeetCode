class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        #Follow this template ONLY
        left = 0
        right = 0
        result = 0
        #count = 0 No need for this since we have used right-left + 1 
        #In cases where left and right are not actually the calculation, we use this count variable
        cost = 0
        while(right<len(s)):
            if s[right] != t[right]:
                cost = cost + abs(ord(s[right])-ord(t[right]))
                while cost>maxCost:
                    cost = cost - abs(ord(s[left])-ord(t[left]))
                    left = left + 1
            result = max(result, right-left+1)
            right = right + 1
        return result
        