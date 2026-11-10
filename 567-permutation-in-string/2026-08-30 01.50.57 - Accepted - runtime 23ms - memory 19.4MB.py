class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        counts1 = Counter(s1)
        counts2 = defaultdict(int)

        for right in range(len(s2)):
            counts2[s2[right]] += 1
            while counts1[s2[right]] < counts2[s2[right]]:
                counts2[s2[left]] -= 1
                left += 1
            
            if right - left + 1 == len(s1):
                return True

        return False