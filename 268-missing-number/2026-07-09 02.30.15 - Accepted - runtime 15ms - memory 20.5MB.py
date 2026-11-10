class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = len(nums) - 1
        ans = 0
        nums.sort()
        if nums[0] != 0:
            return 0
        while i >= 0:
            if nums[i] - nums[i - 1] != 1:
                ans = nums[i - 1] + 1
                return ans
            i -= 1