class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nCol = len(matrix)
        nRow = len(matrix[0])
        rows = set()
        cols = set()


        for r in range(nCol):
            for c in range(nRow):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in range(nCol):
            for c in range(nRow):
                if r in rows or c in cols:
                    matrix[r][c] = 0