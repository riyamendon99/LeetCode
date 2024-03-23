class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left  = 0
        right = 1
        count = 0
        result = 0
        while(right<len(s)):
            if s[right-1]==s[right]:
                count = count + 1
                while count!=1:
                    if s[left] == s[left + 1]:
                        count = count - 1
                    left = left + 1
            result = max(result, right-left+1)
            right = right + 1
        return result

        """if len(s) == 1:
            return 1
        left = 0
        right = 1
        result = 0
        con_count = 0
        digit = s[left]
        while(right<len(s)):
            if s[left] == s[right] and con_count == 0:
                con_count = con_count + 1
            elif s[left] == s[right] and con_count == 1:
                result = left +1
                break
            right = right + 1
            left = left + 1
        if result == 0:
            return len(s)
        return result"""


        