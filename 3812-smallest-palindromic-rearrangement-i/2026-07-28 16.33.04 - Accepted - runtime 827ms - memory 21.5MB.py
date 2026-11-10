class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s = "".join(sorted(s))
        i = 0
        ans = ''
        c = ''
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                ans += s[i]
                i += 2
            else:
                if c == '':
                    c = s[i]
                else:
                    return c
                i += 1
        ans = ans + c + ans[:: - 1]
        return ans
