"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally(horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

# Short Solution
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0

        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    curr = dfs(i, j)
                    result = max(result, curr)
        return result


# Long Solution
class Solution1(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    curr = self.dfs_helper(i, j, grid, visited)
                    result = max(result, curr)
        return result

    def dfs_helper(self, i, j, grid, visited):
        visited.add((i, j))
        if grid[i][j] == 0:
            return 0
        result = 1
        if i > 0 and (i - 1, j) not in visited:
            result += self.dfs_helper(i - 1, j, grid, visited)
        if i < len(grid) - 1 and (i + 1, j) not in visited:
            result += self.dfs_helper(i + 1, j, grid, visited)
        if j > 0 and (i, j - 1) not in visited:
            result += self.dfs_helper(i, j - 1, grid, visited)
        if j < len(grid[0]) - 1 and (i, j + 1) not in visited:
            result += self.dfs_helper(i, j + 1, grid, visited)
        return result
