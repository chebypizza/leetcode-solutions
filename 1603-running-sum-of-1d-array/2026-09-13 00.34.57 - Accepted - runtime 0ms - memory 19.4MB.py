class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSums = [nums[0]]

        for i in range(1, len(nums)):
            prefixSums.append(prefixSums[i - 1] + nums[i])

        return prefixSums