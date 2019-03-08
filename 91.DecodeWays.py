"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        result = [0 for i in range(len(s) + 1)]
        result[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != "0":
                result[i] += result[i - 1]
            if i > 1 and "09" < s[i - 2:i] < "27":
                result[i] += result[i - 2]
        return result[len(s)]


