class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []    #индексы тех, кто не нашел большего

        for i in range(len(nums) * 2):
            curIndex = i % len(nums)
            while stack and nums[stack[-1]] < nums[curIndex]:
                last = stack.pop()
                ans[last] = nums[curIndex]
            if i < len(nums):
                stack.append(i)

        return ans