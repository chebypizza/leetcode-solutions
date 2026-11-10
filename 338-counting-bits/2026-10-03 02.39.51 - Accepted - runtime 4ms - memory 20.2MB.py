class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        num = 1

        for i in range(1, n + 1):
            if num * 2 == i:
                num = i

            dp[i] = dp[i - num] + 1

        return dp