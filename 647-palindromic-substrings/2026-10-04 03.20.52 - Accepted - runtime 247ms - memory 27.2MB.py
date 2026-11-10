class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        counter = 0

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][i] = True
                else:
                    dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])

                if dp[i][j]:
                    counter += 1

        return counter