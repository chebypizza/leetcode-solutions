class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(coloumn, row, index):
            if index == len(word):
                return True

            if (row < 0 or row >= (len(board))) or (coloumn < 0 or coloumn >= len(board[0])):
                return False

            if board[row][coloumn] != word[index]:
                return False

            cur = board[row][coloumn]
            board[row][coloumn] = '*'

            result = backtrack(coloumn + 1, row, index + 1) or backtrack(coloumn - 1, row, index + 1) or backtrack(coloumn, row + 1, index + 1) or \
            backtrack(coloumn, row - 1, index + 1)


            board[row][coloumn] = cur
            return result

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(c, r, 0) == True:
                    return True

        return False