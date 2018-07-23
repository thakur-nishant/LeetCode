"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        pos = 0
        Flag = True
        while True:
            # print(pos, strs[0][:pos])
            if pos < len(strs[0]) and Flag:
                curr = strs[0][pos]
            else:
                break
            for s in strs:
                if pos >= len(s) or s[pos] != curr:
                    Flag = False
                    break
            if not Flag:
                break
            pos += 1

        return strs[0][:pos]

