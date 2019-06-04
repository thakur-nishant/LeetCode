"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        if not coins:
            return -1
        dp = [sys.maxsize - amount] * (amount + 1)
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                if coins[i] == j:
                    dp[j] = 1
                else:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        if dp[amount] > amount:
            return -1
        return dp[amount]

