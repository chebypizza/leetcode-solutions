class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 1
        if x**0 == n:
            return True
        while x <= n:
            x *= 3
            if x == n:
                return True
        return False