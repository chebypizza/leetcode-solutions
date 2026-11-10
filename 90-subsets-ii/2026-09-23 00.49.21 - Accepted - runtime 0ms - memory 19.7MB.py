class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = []
        subset = []
        nums.sort()

        def backtrack(index):
            if index >= len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index + 1)

            subset.pop()

            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1

            backtrack(index + 1)

        backtrack(0)
        return ans