class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        newSet = set()

        for right in range(len(nums)): 
            if nums[right] in newSet:
                return True

            newSet.add(nums[right])

            if right - left >= k:
                newSet.remove(nums[left])
                left += 1

        return False