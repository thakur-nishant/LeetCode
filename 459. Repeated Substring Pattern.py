"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        j = 0
        if len(s) > 1 and s.count(s[0]) == len(s):
            return True
        while j < len(s) // 2 + 1:
            # print(s[j:],s[:-j])
            if s[j:] == s[:-j] and j != len(s) - j - 1:
                return True
            j += 1

        return False


class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]


