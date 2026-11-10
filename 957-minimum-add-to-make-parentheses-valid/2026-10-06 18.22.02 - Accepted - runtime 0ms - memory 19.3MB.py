class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack= []
        
        for i in range(len(s)):
            if s[i] == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack)