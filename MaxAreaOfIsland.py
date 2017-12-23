def findMaxArea(grid, i, j, visited):
    count = 0
    n = len(grid)
    m = len(grid[0])
    visited[i].pop(j)
    visited[i].insert(j, True)

    if i > 0:
        if grid[i - 1][j] == 1 and not visited[i - 1][j]:
            count += 1
            count += findMaxArea(grid, i-1, j, visited)
    if j > 0:
        if grid[i][j - 1] == 1 and not visited[i][j - 1]:
            count += 1
            count += findMaxArea(grid, i, j-1, visited)
    if j+1 < m:
        if grid[i][j + 1] == 1 and not visited[i][j + 1]:
            count += 1
            count += findMaxArea(grid, i, j+1, visited)
    if i+1 < n:
        if grid[i + 1][j] == 1 and not visited[i + 1][j]:
            count += 1
            count += findMaxArea(grid, i+1, j, visited)
    return count

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = []
        n = len(grid)
        m = len(grid[0])
        result = 0
        for i in range(n):
            visited.append([False] * m)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    # visited[i][j] = True
                    count = 1
                    count += findMaxArea(grid, i, j, visited)
                    result = max(result, count)

        # print(result)
        return result


test = Solution()

grid = [[1, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
test.maxAreaOfIsland(grid)
