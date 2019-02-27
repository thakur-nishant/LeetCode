"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        count = 0
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    visited = self.recurse(i, j, visited, grid)
                    count += 1
        return count

    def recurse(self, i, j, visited, grid):
        visited[i][j] = True
        if i > 0 and grid[i - 1][j] == "1" and visited[i - 1][j] is False:
            visited = self.recurse(i - 1, j, visited, grid)
        if j > 0 and grid[i][j - 1] == "1" and visited[i][j - 1] is False:
            visited = self.recurse(i, j - 1, visited, grid)
        if i < len(grid) - 1 and grid[i + 1][j] == "1" and visited[i + 1][j] is False:
            visited = self.recurse(i + 1, j, visited, grid)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == "1" and visited[i][j + 1] is False:
            visited = self.recurse(i, j + 1, visited, grid)
        return visited
