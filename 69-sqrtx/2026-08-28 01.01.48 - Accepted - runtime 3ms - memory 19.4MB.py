class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 0
        right = x // 2

        while left <= right:
            mid = (left + right) // 2
            curSquared = mid * mid
            if curSquared == x:
                return mid
            elif curSquared > x:
                right = mid - 1
            else:
                left = mid + 1

        return right