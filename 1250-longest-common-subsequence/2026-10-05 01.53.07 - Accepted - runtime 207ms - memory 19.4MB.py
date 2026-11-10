class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1, length2 = len(text1), len(text2)

        nextRow = [0] * (length2 + 1)

        for i in range(length1 -1, -1, -1):
            curRow = [0] * (length2 + 1)
            for j in range(length2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    curRow[j] = nextRow[j + 1] + 1
                else:
                    curRow[j] = max(nextRow[j], curRow[j + 1])

            nextRow = curRow

        return nextRow[0]