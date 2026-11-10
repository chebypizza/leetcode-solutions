class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []

        def backtrack(start, subset):
            if len(subset) == k:
                ans.append(subset.copy())
                return

            for i in range(start, n - (k - len(subset)) + 2):
                subset.append(i)
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(1, [])
        return ans