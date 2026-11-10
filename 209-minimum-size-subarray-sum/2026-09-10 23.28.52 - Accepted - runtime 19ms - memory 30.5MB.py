class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum = 0
        left = 0
        bestQuantity = len(nums) + 1

        for right in range(len(nums)):
            curSum += nums[right]
            while curSum >= target:
                bestQuantity = min(right - left + 1, bestQuantity)
                curSum -= nums[left]
                left += 1
        
        if bestQuantity <= len(nums):
            return bestQuantity

        return 0