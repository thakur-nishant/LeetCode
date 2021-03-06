"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        maxword = wordDict[0]
        for word in wordDict:
            if len(word) > len(maxword):
                maxword = word
        max_len = len(maxword)
        wordDict = set(wordDict)

        for i in range(n):
            for j in range(max_len):
                if i - j >= 0 and s[i - j:i + 1] in wordDict and dp[i - j]:
                    dp[i + 1] = True
        return dp[n]


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s and not wordDict:
            return True
        if not s or not wordDict:
            return False

        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        m = max(len(word) for word in words)  # max word size

        for j in range(1, n + 1):
            for i in range(max(0, j - m) + 1, j + 1):
                print(0, j - m, i, s[i-1:j])
                if dp[i - 1] and s[i - 1:j] in words:
                    dp[j] = True
                    break
        print(dp)
        return dp[n]

class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0] = True
        words = set(wordDict)
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
        return dp[-1]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
# s = "applepenapple"
# wordDict = ["apple", "pen"]
x = Solution().wordBreak(s, wordDict)

# This is a recursive solution
"""
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
"""

