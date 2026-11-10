class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        keys = list(counts.keys())
        keys.sort(key = counts.get)
        keys.reverse()
        ar = []
        for i in range(k):
            ar.append(keys[i])
        return ar