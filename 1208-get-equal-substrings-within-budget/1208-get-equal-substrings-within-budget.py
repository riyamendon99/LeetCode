class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        right = 0
        result = 0
        count = 0
        cost = 0
        while(right<len(s)):
            print("Left ", left)
            print("Right ", right)
            if s[right] != t[right]:
                cost = cost + abs(ord(s[right])-ord(t[right]))
                print("Cost ", cost)
                while cost>maxCost:
                    cost = cost - abs(ord(s[left])-ord(t[left]))
                    print("Cost Now ", cost)
                    left = left + 1
                    print("Left Now ", left)
                    print("Right Now ", right)
            result = max(result, right-left+1)
            print("Result ", result)
            right = right + 1
        return result
        