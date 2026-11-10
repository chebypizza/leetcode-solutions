class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = -1
        l = -1
        decA = 0
        decB = 0

        for g in range(len(a)):
            decA += int(a[i]) * 2**g
            i -= 1
        for h in range(len(b)):
            decB += int(b[l]) * 2**h
            l -= 1
        decEnd = decA + decB
        binEnd = bin(decEnd)[2:]
        return binEnd