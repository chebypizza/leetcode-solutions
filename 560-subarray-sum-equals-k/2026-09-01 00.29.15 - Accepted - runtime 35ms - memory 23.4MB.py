class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        dictSeen = defaultdict(int)
        curSum = 0
        dictSeen[0] = 1

        for num in nums:
            curSum += num
            count += dictSeen[curSum - k]

            dictSeen[curSum] += 1

        return count