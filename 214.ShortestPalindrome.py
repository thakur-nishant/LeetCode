"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""


class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or s == s[::-1]:
            return s

        for i in range(len(s) - 1, -1, -1):
            temp = s[i:]
            result = temp[::-1] + s
            if result == result[::-1]:
                return result
