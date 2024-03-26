class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        right = 0
        result = 0
        count = 0
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
        