"""
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        mat = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    mat[i][j] = 1 + mat[i - 1][j - 1]
                else:
                    mat[i][j] = max(mat[i][j - 1], mat[i - 1][j])
        result = m + n - 2 * mat[m][n]
        return result

x = Solution().minDistance('sea','eat')
print(x)
