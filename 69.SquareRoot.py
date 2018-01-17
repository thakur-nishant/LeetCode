"""
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.
"""
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        num = x
        start = 1
        end = x
        while x > 1:
            x = x // 2
            if x ** 2 <= num:
                start = x
                break
            end = x

        for i in range(end - 1, start - 1, -1):
            r = i * i
            if r <= num:
                return i

