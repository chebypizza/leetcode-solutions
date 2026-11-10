class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1, length2 = len(word1), len(word2)

        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        for i in range(1, length2 + 2):
            dp[length1][-i] = i - 1

        for i in range(length1 + 1):
            dp[i][-1] = length1 - i

        for i in range(length1 - 1, -1, -1):
            for j in range(length2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] += min(dp[i + 1][j + 1] + 1, dp[i][j + 1] + 1, dp[i + 1][j] + 1)

        return dp[0][0]