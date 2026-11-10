class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        w = 1
        while w < n:
            for lo in range(0, n, 2*w):
                L = nums[lo : lo+w]
                R = nums[lo+w : lo + 2*w]
                nums[lo : lo+2*w] = merge(L, R)
            w *= 2

        return nums