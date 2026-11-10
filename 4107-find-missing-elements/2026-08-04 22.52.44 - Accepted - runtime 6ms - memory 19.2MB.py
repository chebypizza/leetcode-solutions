class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ar = []
        for i in range(len(nums) - 1):
            cur = nums[i]
            next = nums[i + 1]
            if cur + 1 != next:
                while cur + 1 != next:
                    ar.append(cur + 1)
                    cur = cur + 1
        return ar