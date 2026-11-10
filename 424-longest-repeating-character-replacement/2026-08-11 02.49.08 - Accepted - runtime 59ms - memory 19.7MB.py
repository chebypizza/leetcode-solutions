class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxCount = 0
        dict = defaultdict(int)

        for right in range(len(s)):
            dict[s[right]] += 1

            maxCount = max(maxCount, dict[s[right]])

            if (right - left + 1) - maxCount > k:
                dict[s[left]] -= 1
                left += 1

        return right - left + 1
