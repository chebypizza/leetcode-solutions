class Solution:
    def checkString(self, s: str) -> bool:
        start = False
        
        for i in range(len(s)):
            if s[i] == 'b':
                start = True
                continue
            
            if start and s[i] == 'a':
                return False
        
        return True