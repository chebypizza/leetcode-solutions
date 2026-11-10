class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        ar = []
        while i < len(nums1):
            if nums1[i] in nums2:
                if nums1[i] not in ar:
                    ar.append(nums1[i])
            i += 1
        return ar
