class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        subset = []

        def backtrack(start):
            if start == len(s):
                ans.append(subset.copy())
                return

            for i in range(start, len(s)):
                if s[start:i + 1] != s[start:i + 1][::-1]:
                    continue
                subset.append(s[start:i + 1])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return ans