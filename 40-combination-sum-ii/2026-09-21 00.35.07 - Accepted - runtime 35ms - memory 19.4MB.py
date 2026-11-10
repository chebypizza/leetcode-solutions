class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        subset = []
        candidates.sort()

        def backtrack(index, curSum):
            if curSum == target:
                ans.append(subset.copy())
                return

            if index >= len(candidates):
                return

            if curSum > target:
                return

            subset.append(candidates[index])
            backtrack(index + 1, curSum + candidates[index])

            subset.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            backtrack(index + 1, curSum)

        backtrack(0, 0)
        return ans