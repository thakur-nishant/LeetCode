"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Eg.
digits = [1,1]

result = [1,2]
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        number = 0
        for digit in digits:
            number = number * 10 + digit

        number += 1

        while number > 0:
            result.insert(0, number % 10)
            number = number // 10

        return result
