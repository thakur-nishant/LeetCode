"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        st = ""
        for x in wordDict:
            if x in s:
                start = s.index(x)
                end = start + len(x) - 1
                left = right = True
                if start > 0:
                    left = self.wordBreak(s[:start], wordDict)
                if end < len(s) - 1:
                    right = self.wordBreak(s[end + 1:], wordDict)

                if left and right:
                    return True

        return False
