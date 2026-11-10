class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        subset = []
        seen = set()

        def backtrack():            
            if len(subset) == len(nums):
                ans.append(subset.copy())
                return

            for num in nums:
                if num in seen:
                    continue
                subset.append(num)
                seen.add(num)
                backtrack()
                subset.pop()
                seen.remove(num)

        backtrack()
        return ans