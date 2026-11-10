class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        isNegative = False

        if x < 0:
            isNegative = True
            x *= -1

        while x > 0:
            cur = x % 10
            ans = ans * 10 + cur
            x = x // 10

        if isNegative == True:
            ans *= -1

        if ans < -2**31 or ans > 2**31 - 1:
            return 0

        return ans