class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
            
        longest = ''
        dp = [[False] * size for _ in range(size)] 

        for i in range(size - 1, -1, -1):
            for j in range(i, size):
                if i == j:
                    dp[i][i] = True
                elif j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j]:
                    palindrome = s[i:j + 1]
                    if len(palindrome) > len(longest):
                        longest = palindrome

        return longest