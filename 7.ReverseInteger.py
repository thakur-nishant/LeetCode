"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            s = str(x)[1:]
            num = -1 * int(s[::-1])
        else:
            s = str(x)
            num = int(s[::-1])

        if num > 2147483647 or num < -2147483648:
            return 0
        else:
            return num

