class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        minSc = nums[-1]

        for i in range(3):
            minSc = min(minSc, nums[i + n - 2 - 1] - nums[i])

        return minSc