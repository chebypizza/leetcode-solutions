class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        n -= 10
        AliceTurn = False

        for i in range(9, 0, -1):
            n -= i
            AliceTurn = not AliceTurn
            if n < 0 and AliceTurn:
                return True
            if n < 0 and not AliceTurn:
                return False

        return AliceTurn