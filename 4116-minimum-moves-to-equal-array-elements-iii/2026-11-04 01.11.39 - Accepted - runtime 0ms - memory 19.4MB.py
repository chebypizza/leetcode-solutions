class Solution:
    def minMoves(self, nums: List[int]) -> int:
        goal = max(nums)
        ans = 0

        for num in nums:
            ans += num - goal

        return abs(ans)