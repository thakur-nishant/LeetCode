"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = {}
        n = len(s)
        num = 1
        for i in range(ord('A'), ord('Z') + 1):
            alpha[chr(i)] = num
            num += 1

        result = 0
        for i in range(n):
            result += 26 ** i * alpha[s[n - i - 1]]

        return result

