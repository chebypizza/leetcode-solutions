class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    empty.append((r,c))
                else:
                    boxId = (r // 3) * 3 + (c // 3)
                    rows[r].add(num)
                    cols[c].add(num)
                    blocks[boxId].add(num)
        
        def check(board, row, col, strI, boxId):
            if strI in rows[row] or strI in cols[col] or strI in blocks[boxId]:
                return False

            return True

        def solver(emptyCell):
            if emptyCell == len(empty):
                return True

            row, col = empty[emptyCell] 

            boxId = (row // 3) * 3 + (col // 3)
            for i in range(1, 10):
                strI = str(i)
                if check(board, row, col, strI, boxId):
                    board[row][col] = strI
                    rows[row].add(strI)
                    cols[col].add(strI)
                    blocks[boxId].add(strI)

                    if solver(emptyCell + 1):
                        return True

                    board[row][col] = '.'
                    rows[row].remove(strI)
                    cols[col].remove(strI)
                    blocks[boxId].remove(strI)

        solver(0)