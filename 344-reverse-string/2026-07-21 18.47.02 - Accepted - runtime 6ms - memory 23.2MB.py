class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        while i < len(s) // 2:
            left = s[i]
            right = s[-i - 1]
            s[i] = right
            s[-i - 1] = left
            i += 1