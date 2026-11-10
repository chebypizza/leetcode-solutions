class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        counter = 0

        for i in range(len(nums) // 2):
            counter += nums[-(i + 1)] - nums[i]

        return counter