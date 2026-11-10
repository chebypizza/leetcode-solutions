class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        summ = 0
        l = len(nums) - 1
        summ += nums[l] - 1
        l -= 1
        summ *= nums[l] -1
        return summ