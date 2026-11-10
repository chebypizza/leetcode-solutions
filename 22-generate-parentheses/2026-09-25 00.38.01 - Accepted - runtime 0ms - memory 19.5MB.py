class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(cur, counterOpen, counterClosed):
            if len(cur) == n * 2 and counterOpen == counterClosed:
                ans.append(cur)
                return
            
            if counterOpen < n:
                backtrack(cur + '(', counterOpen + 1, counterClosed)

            if counterClosed < counterOpen:
                backtrack(cur + ')', counterOpen, counterClosed + 1)

        backtrack('', 0, 0)
        return ans