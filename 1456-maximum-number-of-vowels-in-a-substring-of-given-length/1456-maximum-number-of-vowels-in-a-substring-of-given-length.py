class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_count = 0
        max_count = 0
        while right<len(s):
            if right-left == k:
                #max_count = vowel_count
                if s[left] in vowels:
                    vowel_count = vowel_count -1
                left = left + 1
            if s[right] in vowels:
                vowel_count = vowel_count + 1
                max_count = max(max_count, vowel_count)
            right = right + 1
        return max_count

        