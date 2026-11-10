class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        subset = []

        def backtrack(index, curSum):
            if index >= len(candidates):
                return 

            if curSum > target:
                return

            if curSum == target:
                ans.append(subset.copy())
                return
            
            subset.append(candidates[index])
            backtrack(index, curSum + candidates[index])

            subset.pop()
            backtrack(index + 1, curSum)

        backtrack(0, 0)
        return ans