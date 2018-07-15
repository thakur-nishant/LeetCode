"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        i = rows // 2
        j = cols // 2
        visited = {}
        while True:
            key = tuple([i,j])
            if key in visited:
                break
            else:
                visited[key] = 1
            print(key,matrix[i][j])
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                if i > 0 and target <= matrix[i-1][j]:
                    i -= 1
                    j -= 1
                else:
                    j -= 1
                if j < 0:
                    j = cols-1
            else:
                if i < rows-1 and target >= matrix[i+1][j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                if j >= cols:
                    j = 0
        return False


m= [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target =  50
x = Solution().searchMatrix(m, target)
print(x)
