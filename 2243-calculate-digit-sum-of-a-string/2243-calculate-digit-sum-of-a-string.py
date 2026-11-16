class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            curS = ''
            for i in range(0, len(s), k):
                curSum = sum(int(x) for x in s[i:i + k])
                curS += str(curSum)
            s = curS

        return s