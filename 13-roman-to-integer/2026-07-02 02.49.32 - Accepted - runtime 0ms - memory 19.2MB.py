class Solution:
    def romanToInt(self, s: str) -> int:
        b = len(s)
        res = 0
        i = b - 1
        while i >= 0:
            if s[i] == 'M':
                if i > 0 and s[i - 1] == 'C':
                    res += 900
                    i -= 1
                else:
                    res += 1000
            elif s[i] == 'D':
                if i > 0 and s[i - 1] == 'C':
                    res += 400
                    i -= 1
                else:
                    res += 500
            elif s[i] == 'C':
                if i > 0 and s[i - 1] == 'X':
                    res += 90
                    i -= 1
                else:
                    res += 100
            elif s[i] == 'L':
                if i > 0 and s[i - 1] == 'X':
                    res += 40
                    i -= 1
                else:
                    res += 50
            elif s[i] == 'X':
                if i > 0 and s[i - 1] == 'I':
                    res += 9
                    i -= 1
                else:
                    res += 10
            elif s[i] == 'V':
                if i > 0 and s[i - 1] == 'I':
                    res += 4
                    i -= 1
                else:
                    res += 5
            elif s[i] == 'I':
                res += 1
            i -= 1
        return res
