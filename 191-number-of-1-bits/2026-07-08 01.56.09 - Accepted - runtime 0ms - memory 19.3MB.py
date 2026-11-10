class Solution:
    def hammingWeight(self, n: int) -> int:
        a = str(bin(n)[2:])
        i = len(a) - 1
        quantity = 0
        while i >= 0:
            if a[i] == '1':
                quantity += 1
            i -= 1
        return quantity