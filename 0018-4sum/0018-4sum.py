class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = set()

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                t, f = j + 1, n - 1
                while t < f:
                    fourSum = nums[i] + nums[j] + nums[t] + nums[f]
                    if fourSum == target:
                        ans.add((nums[i], nums[j], nums[t], nums[f]))
                        t += 1
                        f -= 1
                    elif fourSum < target:
                        t += 1
                    else:
                        f -= 1

        return list(ans)