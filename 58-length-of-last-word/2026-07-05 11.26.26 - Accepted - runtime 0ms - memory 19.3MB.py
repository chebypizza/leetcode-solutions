class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        d = s.replace(" ","")
        while s[i] == ' ':
            i -=1
        lengthWithoutSpace = len(d)
        if lengthWithoutSpace > 1:
                if len(s) != lengthWithoutSpace:
                    while s[i] != ' ':
                        i -= 1
                        length += 1
                else:
                    length += len(s)
        else:
            length += 1

        return length