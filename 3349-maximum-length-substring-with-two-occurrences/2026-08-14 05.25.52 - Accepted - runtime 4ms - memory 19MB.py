class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        dict = defaultdict(int)

        for right in range(len(s)):
           dict[s[right]] += 1

           while dict[s[right]] > 2:
            dict[s[left]] -= 1
            left += 1

           maxLength = max(maxLength, right - left + 1)

        return maxLength