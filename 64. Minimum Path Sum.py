"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = [[0] * (len(grid[0])) for _ in range(len(grid))]

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    result[i][j] = grid[i][j]
                elif i == len(grid) - 1:
                    result[i][j] = grid[i][j] + result[i][j + 1]
                elif j == len(grid[0]) - 1:
                    result[i][j] = grid[i][j] + result[i + 1][j]
                else:
                    result[i][j] = grid[i][j] + min(result[i + 1][j], result[i][j + 1])
        return result[0][0]

