class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        ans = ''

        for letters in zip(*strs):
            if len(set(letters)) == 1:
                ans += letters[0]
            else:
                break

        return ans