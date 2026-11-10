class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        if x <= 0:
            return False
        while x <= n:
            if x == n:
                return True
            x *= 2
        return False