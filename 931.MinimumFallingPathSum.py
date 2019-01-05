"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.



Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation:
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.



Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""

class Solution:

    ####################################
    ##  Dynamic programming Solution  ##
    ####################################
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        while len(A) >= 2:
            row = A.pop()
            for i in range(len(row)):
                A[-1][i] += min(row[max(0, i - 1): min(len(row), i + 2)])
        return min(A[0])
    ####################################
    ## Recursive Brute-Force Solution ##
    ####################################
    def minFallingPathSum_DFS(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        result = []
        if len(A) == 1:
            return min(A[0])
        for col, num in enumerate(A[0]):
            self.recurse(result, A, 1, col, num)
        # print(result)
        return min(result)

    def recurse(self, result, A, nxtpt, col, currsum):
        if nxtpt == len(A) - 1:
            result.append(currsum + A[nxtpt][col])
            if col > 0:
                result.append(currsum + A[nxtpt][col - 1])
            if col < len(A) - 1:
                result.append(currsum + A[nxtpt][col + 1])
        else:
            self.recurse(result, A, nxtpt + 1, col, currsum + A[nxtpt][col])
            if col > 0:
                self.recurse(result, A, nxtpt + 1, col - 1, currsum + A[nxtpt][col - 1])
            if col < len(A) - 1:
                self.recurse(result, A, nxtpt + 1, col + 1, currsum + A[nxtpt][col + 1])
        return


x = Solution()
A = [[-80,-13,22],[83,94,-5],[73,-48,61]]
test = x.minFallingPathSum(A)
print("Result:", test)

