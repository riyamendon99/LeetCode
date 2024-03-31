class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        left = 0
        right = 1
        vowels = 'aeiou'
        order = {char:idx for idx, char in enumerate(vowels)}
        count = 0
        while(right<len(word)):
            if word[left] == 'a' and ((order[word[right-1]]==order[word[right]]) or (order[word[right-1]]+1 == order[word[right]])):
                right += 1
            else:
                left = right
                right += 1
            if word[right-1] == 'u' and word[left] == 'a':
                count = max(count, (right-1)-left + 1)
        return count
        """left = 0
        right = 1
        count = 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        while(right<len(word)):
            print("rrrright ", word[right])
            print("lllleft ", word[left])
            if word[right] not in vowel or word[left] != 'a' or (word[right-1] == 'a' and word[right]!='a') or (word[right-1] == 'a'and word[right]!='e'):
                print("right is ", right)
                while(left<right):
                    left = left + 1
            print("right here is ", right)
            print("left is ", left)
            count = max(count, right-left + 1)
            right = right + 1
        return count"""
        