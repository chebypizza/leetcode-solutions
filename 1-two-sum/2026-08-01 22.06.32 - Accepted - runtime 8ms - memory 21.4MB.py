class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = defaultdict(list)

        for i, g in enumerate(nums):
            dict[g].append(i)
        
        nums.sort()
        l = 0
        r = len(nums) - 1

        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                if nums[l] != nums[r]:
                    first = dict[nums[l]][0]
                    second = dict[nums[r]][0]
                    return [first, second]
                else:
                    first = dict[nums[l]][0]
                    second = dict[nums[l]][1]
                    return [first,second]
            if sum < target:
                l += 1
            else:
                r -= 1
        return []