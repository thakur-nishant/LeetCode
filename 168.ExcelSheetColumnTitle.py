"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        A_to_Z = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

        result = ""
        r = 0
        while n > 0:
            n = n - 1
            r = n % 26
            n = n // 26
            result = str(A_to_Z[r]) + result

        return result


test = Solution()

x = test.convertToTitle(26)
print(x)
