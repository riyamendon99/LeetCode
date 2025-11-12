class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        while left < right:
            print(left)
            print(right)
            while((left>= 0 and left<=len(s)-1) and not(s[left]>= 'A' and s[left]<='Z') and not(s[left]>= 'a' and s[left]<='z') and not(s[left]>= '0' and s[left]<='9')):
                left += 1
            while((right>=0 and right<=len(s)-1) and not(s[right]>= 'A' and s[right]<='Z') and not(s[right]>= 'a' and s[right]<='z') and not(s[right]>= '0' and s[right]<='9')):
                right -= 1
            if((left>= 0 and left<=len(s)-1) and (right>=0 and right<=len(s)-1)):
                if(s[left].lower() == s[right].lower()):
                    left += 1
                    right -= 1
                else:
                    return False
        return True
        