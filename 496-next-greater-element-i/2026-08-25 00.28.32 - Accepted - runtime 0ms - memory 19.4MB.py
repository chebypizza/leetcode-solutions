class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        stack = []
        dict = {}

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                last = stack.pop()       #индекс числа, которомсу нашлось большее
                dict[nums2[last]] = nums2[i]
            stack.append(i)

        for l in range(len(ans)):
            ans[l] = dict.get(nums1[l], -1)       

        return ans