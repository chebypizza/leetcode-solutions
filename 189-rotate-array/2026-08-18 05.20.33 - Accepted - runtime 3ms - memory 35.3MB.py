class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        k %= len(nums)

        stack = nums[-k:]

        del nums[-k:]

        nums[:0] = stack