class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
                
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                curSum = nums[left] + nums[right] + nums[i]
                
                if curSum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curSum > 0:
                    right -= 1
                else:
                    left += 1
        
        return ans 