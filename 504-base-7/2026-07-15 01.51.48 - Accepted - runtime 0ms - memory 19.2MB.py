class Solution:
    def convertToBase7(self, num: int) -> str:
        num2 = num
        ans = ''
        if num < 0:
            num *= -1
        while num >= 7:
            ans += str(num % 7)
            num = num // 7
        ans += str(num % 7)
        num = num // 7
        ans = ans[::-1]
        if num2 < 0:
            ans = '-' + ans
        return ans