class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        dictionary = {}
        l = 0

        for right in range(len(s)):
            if s[right] in dictionary and dictionary[s[right]] >= left:
                left = dictionary[s[right]] + 1
            dictionary[s[right]] = right
            if l <= right - left + 1:
                l = right - left + 1

        return l