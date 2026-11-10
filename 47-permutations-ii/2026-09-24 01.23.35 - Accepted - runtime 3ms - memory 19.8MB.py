class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        subset = []
        n = len(nums)
        used = [False] * n
        nums.sort()

        def backtrack():
            if len(subset) == n:
                ans.append(subset.copy())
                return

            for i in range(n):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                subset.append(nums[i])
                backtrack()
                used[i] = False
                subset.pop()

        backtrack()
        return ans