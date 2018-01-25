"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in range(rowIndex):
            row = i + 1
            for j in range(row - 1):
                result[j] += result[j + 1]
            result.insert(0, 1)
            # print(result)

        return result
