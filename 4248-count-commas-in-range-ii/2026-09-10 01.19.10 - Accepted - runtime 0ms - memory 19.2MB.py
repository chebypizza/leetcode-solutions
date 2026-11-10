class Solution:
    def countCommas(self, n: int) -> int:
        num = 1000
        ans = 0

        while n >= num:
            ans += (n - num + 1)
            num *= 1000

        return ans