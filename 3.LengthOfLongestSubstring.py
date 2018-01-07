"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        loc = {}
        result = 0
        j = 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            if s[i] in loc:
                j = max(j, loc[s[i]])
            result = max(result, i - j + 1)
            loc[s[i]] = i + 1

        print(result)
        return result


test = Solution()
test.lengthOfLongestSubstring('abxabccbqwertyy')