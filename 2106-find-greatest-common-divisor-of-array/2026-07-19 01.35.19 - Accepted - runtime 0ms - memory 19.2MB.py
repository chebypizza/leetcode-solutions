class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        sml = nums[0]
        lrg = nums[-1]
        i = sml
        while i > 0:
            if sml % i == 0 and lrg % i == 0:
                return i
            i -= 1