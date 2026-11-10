class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i = 0
        l1, l2 = len(word1), len(word2)

        while i < l1 or i < l2:
            if i < l1:
                ans.append(word1[i])
            if i < l2:
                ans.append(word2[i])
            i += 1

        return "".join(ans)