class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        curSum = 0
        dictSeen = defaultdict(int)
        dictSeen[0] = 1

        for num in nums:
            curSum += num
            count += dictSeen[curSum % k]
            dictSeen[curSum % k] += 1

        return count