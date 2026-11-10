class Solution:
    def isValid(self, s: str) -> bool:
        ar = []
        reversedBrackets = [')', '}', ']']
        if len(s) % 2 != 0 or s[-1] not in reversedBrackets:
            return False
        brackets = {
            ')': '(',
            '(': ')',
            '{': '}',
            '}': '{',
            '[': ']',
            ']': '['
        }
        i = 0
        while i < len(s):
            if s[i] in reversedBrackets:
                if len(ar) == 0:
                    return False
                bracket = ar[-1]
                flipped = brackets.get(bracket, bracket)
                if len(ar) >= 1 and flipped == s[i]:
                    ar.pop(-1)
                else:
                    return False
            else:
                ar.append(s[i])
            i += 1
        if len(ar) != 0:
            return False
        else:
            return True