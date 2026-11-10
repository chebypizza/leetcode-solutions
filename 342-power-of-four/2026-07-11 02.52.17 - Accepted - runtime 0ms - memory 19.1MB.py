class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 1
        if n <= 0:
            return False
        while x<=n:
            if x == n:
                return True
            x *= 4
        return False