class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        def robber(start:int, end:int) -> int:
            dp = [0] * n
            dp[start] = nums[start]
            dp[start + 1] = max(nums[start], nums[start + 1])

            for i in range(start + 2, end):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

            return dp[end - 1]

        caseOne = robber(0, n - 1)

        caseTwo = robber(1, n)

        return max(caseOne, caseTwo)