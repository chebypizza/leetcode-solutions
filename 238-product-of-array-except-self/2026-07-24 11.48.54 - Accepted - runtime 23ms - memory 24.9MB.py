class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ar = []
        summ = 1
        zero = 0
        for i in nums:
            if i == 0:
                zero += 1
                continue
            summ *= i
        l = 0
        while l < len(nums):
            if nums[l] == 0 and zero < 2:
                newS = summ
            elif zero > 0:
                newS = 0
            else:
                newS = summ // nums[l]
            ar.append(newS)
            l += 1
        return ar