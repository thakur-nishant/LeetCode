"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not any(matrix):
            return []
        result = []
        hs = vs = 0
        he = len(matrix[0]) - 1
        ve = len(matrix) - 1
        while hs <= he and vs <= ve:
            for j in range(hs, he + 1):
                result.append(matrix[vs][j])
            vs += 1
            for i in range(vs, ve + 1):
                result.append(matrix[i][he])
            he -= 1
            if vs <= ve:
                for j in range(he, hs - 1, -1):
                    result.append(matrix[ve][j])
                ve -= 1
            if hs <= he:
                for i in range(ve, vs - 1, -1):
                    result.append(matrix[i][hs])
                hs += 1
        return result


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return matrix
        row = len(matrix)
        col = len(matrix[0])
        i = j = 0
        result = []
        while row > 0 or col > 0:
            temp = col
            while temp > 0 and row > 0 and col > 0:
                print(matrix[i][j])
                result.append(matrix[i][j])
                j += 1
                temp -= 1
            j -= 1
            row -= 1
            i += 1
            print("going down",row,col)
            temp = row
            while temp > 0 and row > 0 and col > 0:
                print(matrix[i][j])
                result.append(matrix[i][j])
                i += 1
                temp -= 1
            i -= 1
            col -= 1
            j -= 1
            print("going left",row,col)
            temp = col
            while temp > 0 and row > 0 and col > 0:
                print(matrix[i][j])
                result.append(matrix[i][j])
                j -= 1
                temp -= 1
            j += 1
            row -= 1
            i -= 1
            print("going up",row,col)
            temp = row
            while temp > 0 and row > 0 and col > 0:
                print(matrix[i][j])
                result.append(matrix[i][j])
                i -= 1
                temp -= 1
            i += 1
            col -= 1
            j += 1
            print("going right",row,col)

        return result

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[6,9,7]]
x = Solution().spiralOrder(matrix)
print(x)

