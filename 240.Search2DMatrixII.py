"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


####################################
##         Basic Solution         ##
####################################

class SolutionBasic:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = col = 0
        while row < len(matrix):
            while col < len(matrix[0]):
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    col = 0
                    row += 1
                else:
                    col += 1
        return False


####################################
##     Binary Search Solution     ##
####################################

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = col = 0
        while row < len(matrix):
            if self.binarySearch(matrix[row], target):
                return True
            else:
                row += 1
        return False

    def binarySearch(self, arr, target):
        if not arr:
            return False

        root_pt = len(arr) // 2
        if arr[root_pt] == target:
            return True
        elif target < arr[root_pt]:
            return self.binarySearch(arr[:root_pt], target)
        else:
            if root_pt + 1 < len(arr):
                return self.binarySearch(arr[root_pt + 1:], target)
            return False


