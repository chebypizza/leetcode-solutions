class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #123 + 1, 123 + 1, 12 + 1, 12 + 1
        if numRows == 1:
            return s
            
        ans = []
        n = len(s)
        cycle = 2 * numRows - 2

        for r in range(numRows):
            for i in range(r, n, cycle):
                ans.append(s[i])
                if 0 < r < numRows - 1:
                    nextInTheRow = i + cycle - 2 * r
                    if nextInTheRow < n:
                        ans.append(s[nextInTheRow])

        return "".join(ans)