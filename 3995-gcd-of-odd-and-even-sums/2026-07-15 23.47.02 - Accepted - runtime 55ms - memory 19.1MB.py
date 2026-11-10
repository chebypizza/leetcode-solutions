class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        for i in range(n):
            k = 2 * i
            sumOdd += 1 + k
            sumEven += 2 + k
        if sumOdd >= sumEven:
            GCD = sumOdd
            g = sumOdd - sumEven
        else:
            GCD = sumEven
            g = sumEven - sumOdd
        while GCD >= g:
            if sumOdd % GCD == 0 and sumEven % GCD == 0:
                return GCD
            else:
                GCD -= g