class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        theSmallestOne = prices[0]
        profit = 0

        for i in prices:
            if i < theSmallestOne:
                theSmallestOne = i
            profit = max(i - theSmallestOne, profit)

        return profit