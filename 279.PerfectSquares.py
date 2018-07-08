"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

import sys


class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = {}
        sqrt_list = []
        for i in range(1, n + 1):
            counts[i] = 0
        i = 1
        s = 1
        while s <= n:
            sqrt_list.append(s)
            counts[s] = 1
            i += 1
            s = i * i
        print(sqrt_list)
        result = self.generateCombinations(n, sqrt_list[::-1], counts, 0)
        print(counts)
        return result

    def generateCombinations(self, n, sqrt_list, counts, count):
        min_count = sys.maxsize
        if counts[n]:
            return count + counts[n]
        for num in sqrt_list:
            if num < n:
                res = self.generateCombinations(n - num, sqrt_list, counts, count + 1)
                min_count = min(min_count, res)
        counts[n] = min_count - count
        return min_count


x = Solution().numSquares(562)
print(x)
