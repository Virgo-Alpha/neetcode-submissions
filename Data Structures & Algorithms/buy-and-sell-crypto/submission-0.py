class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0

        for sell in range(len(prices)):
            #  if we find a lower buying price than my current buying price
            if prices[sell] < prices[buy]:
                buy = sell
            # max profit after every transaction
            profit = max(profit, (prices[sell] - prices[buy]))

        return profit
