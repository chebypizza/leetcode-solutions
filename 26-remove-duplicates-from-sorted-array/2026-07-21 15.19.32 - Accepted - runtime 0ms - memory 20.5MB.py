class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums) - 1
        while l > 0:
            if nums[l] == nums[l - 1]:
                nums.pop(l)
            l -=1