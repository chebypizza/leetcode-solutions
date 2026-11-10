class Solution:
    def maxProduct(self, n: int) -> int:
        i = 0
        nStr = str(n)
        ar = []
        while i < len(nStr):
            ar.append(nStr[i])
            i += 1
        ar.sort()
        answer = int(ar[-1]) * int(ar[-2])
        return answer