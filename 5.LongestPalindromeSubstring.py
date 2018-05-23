"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            plen = max(len1, len2)
            if plen > end - start + 1:
                start = i - (plen - 1) // 2
                end = i + plen // 2

        return s[start:end + 1]

    #         if not s or s == s[::-1]:
    #             return s

    #         left_string = self.longestPalindrome(s[:-1])
    #         right_string = self.longestPalindrome(s[1:])

    #         if len(left_string) >= len(right_string):
    #             return left_string

    #         return right_string

    def expandAroundCenter(self, s, L, R):
        while (L >= 0 and R < len(s) and s[L] == s[R]):
            L -= 1
            R += 1
        return R - L - 1

