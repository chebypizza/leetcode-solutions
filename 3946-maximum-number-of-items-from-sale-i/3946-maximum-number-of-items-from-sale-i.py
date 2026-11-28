class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        profit = []
        n = len(items)

        for i in range(n):
            cur = items[i]
            curProfit = 1
            for j in range(n):
                if i != j:
                    check = items[j]
                    if check[0] % cur[0] == 0:
                        curProfit += 1
            profit.append(curProfit)

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            price = items[i][1]
            for j in range(budget, price - 1, -1):
                if dp[j - price] != -1:
                    dp[j] = max(dp[j], dp[j - price] + profit[i])
        
        ans = 0
        minPrice = 1500
        for i in range(n):
            minPrice = min(minPrice, items[i][1])
        
        for i in range(budget + 1):
            if dp[i] != -1:
                ans = max(ans, dp[i] + (budget - i) // minPrice)

        return ans