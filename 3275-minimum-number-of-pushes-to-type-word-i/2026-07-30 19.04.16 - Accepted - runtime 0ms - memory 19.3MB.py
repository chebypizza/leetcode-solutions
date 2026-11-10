class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        print(l)
        if l <= 8:
            return l
        elif l <= 16:
            ans = l - 8
            return ans * 2 + 8
        elif l <= 24:
            ans = l - 16
            return ans * 3 + 24
        else:
            ans = l - 24
            return ans * 4 + 48