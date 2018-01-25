"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        result = [[1]]
        for i in range(numRows - 1):
            last_row = len(result) - 1
            new_row = [1, 1]
            j = last_row
            k = 1
            while j > 0:
                new_row.insert(k, result[last_row][k - 1] + result[last_row][k])
                k += 1
                j -= 1

            result.append(new_row)

        return result
    
