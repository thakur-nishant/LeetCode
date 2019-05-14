/*
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]


Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
*/

class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int n = matrix.length;
        if (n == 0) return matrix;
        int m = matrix[0].length;
        if (m == 0) return matrix;

        int[][] result = new int[n][m];
        int max_val = n*m;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (matrix[i][j] != 0) {
                    int top = (i > 0)? result[i-1][j]:max_val;
                    int left = (j > 0)? result[i][j-1]:max_val;
                    result[i][j] = 1 + Math.min(top,left);
                }
            }
        }
        for (int i = n-1; i >= 0; --i) {
            for (int j = m-1; j >= 0; --j) {
                if (matrix[i][j] != 0) {
                    int bot = (i < n-1)? result[i+1][j]:max_val;
                    int right = (j < m-1)? result[i][j+1]:max_val;
                    result[i][j] = Math.min(1 + Math.min(bot,right), result[i][j]);
                }
            }
        }
        return result;
    }
}