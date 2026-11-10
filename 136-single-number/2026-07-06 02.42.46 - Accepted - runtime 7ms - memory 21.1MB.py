class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = len(nums) - 1
        nums.sort()
        numb = 0
        while i > 0:
            if nums[i] != nums[i - 1] and i > 1:
                return nums[i]
            i -= 2
        return nums[i]