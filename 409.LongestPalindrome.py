"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        for i in s:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        flag = False
        result = 0
        for key in counter:
            if counter[key] % 2 == 0:
                result += counter[key]
            else:
                result += counter[key] - 1
                flag = True
        if flag:
            result += 1
        return result

