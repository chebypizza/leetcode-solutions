class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = str(bin(n))
        i = len(x) - 1
        while i > 0:
            if x[i] == x[i - 1]:
                return False
            i -= 1
        return True