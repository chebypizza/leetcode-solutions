class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        #low - индекс самого мелкого числа

        if target == nums[low]:
            return low
        elif target > nums[low] and target <= nums[-1]:
            high = len(nums) - 1
        else:
            high = low - 1
            low = 0

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1