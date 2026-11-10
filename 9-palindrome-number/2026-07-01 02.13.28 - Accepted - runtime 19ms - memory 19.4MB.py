class Solution:
    def isPalindrome(self, x: int) -> bool:
        b = str(x)
        left = -1
        right = 0

        for i in range(len(b)):
            if b[left] == b[right]:
                right += 1
                left -= 1
            else:
                return False
        return True
