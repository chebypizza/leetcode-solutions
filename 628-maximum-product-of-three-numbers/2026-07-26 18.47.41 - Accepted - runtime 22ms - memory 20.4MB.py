class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        ans1 = ans2 = 1
        length = len(nums)
        i = length - 1
        for l in range(2):
            ans1 *= nums[i]
            ans2 *= nums[l]
            i -= 1
        ans1 *= nums[i]
        ans2 *= nums[length - 1]
        if ans1 >= ans2:
            return ans1
        else:
            return ans2