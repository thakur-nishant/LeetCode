"""
Say you have an array for which the i'th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
import sys
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell1 = sell2 = 0
        buy1 = buy2 = - sys.maxsize

        for i in range(len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return sell2


test = Solution()
p = [7,1,5,3,6,4]
x = test.maxProfit(p)
print(x)

