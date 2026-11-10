class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #если доходим до конца t, то сдвигаем left, пока dict(s) != dict(t), если не нашли 2 ранвых словаря, то продолжаем двигать right, пока left стоит на месте
        left = 0
        counts1 = defaultdict(int)
        counts2 = Counter(t)
        minWindow = 100000
        needed = len(counts2)
        now = 0

        for right in range(len(s)):
            counts1[s[right]] += 1
            if s[right] in counts2 and counts2[s[right]] == counts1[s[right]]:
                now += 1
                while left <= right and now == needed:
                    if minWindow > right - left + 1:
                        minWindow = right - left + 1
                        startIndex = left
                        endIndex = right

                    if counts2[s[left]] == counts1[s[left]]:
                        now -= 1

                    counts1[s[left]] -= 1
                    left += 1
            right += 1
        
        if minWindow != 100000:
            return s[startIndex:endIndex + 1]

        return ''