class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) / 3
        ans = []
        
        for key, value in Counter(nums).items():
            if value > n:
                ans.append(key)   

        return ans