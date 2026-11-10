class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ar = []
        nums.sort()
        i = len(nums) - 1
        length = 1
        while i > 0:
            if nums[i] == nums[i - 1]:
                nums.pop(i - 1)
            i -= 1
        l = len(nums) - 1
        while l >= 0:
            if nums[-l] == nums[-l - 1] + 1:
                length += 1
            else:
                ar.append(length)
                length = 1
            l -= 1
        theBiggestOne = 0
        j = 0
        while j < len(ar):
            if theBiggestOne <= ar[j]:
                theBiggestOne = ar[j]
            j += 1
        return theBiggestOne