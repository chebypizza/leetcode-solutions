class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = len(s) - 1
        i = 0
        while i < l:
            if s[i] != s[l]:
                left = s[i + 1:l + 1]
                right = s[i : l]
                if left == left[::- 1] or right == right[::-1]:
                    return True
                else:
                    return False
            l -= 1
            i += 1
        return True