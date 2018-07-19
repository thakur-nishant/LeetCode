"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0
        n = len(s)
        max_length = 0
        distinct = {}
        while i < n and j < n:
            while j < n:
                if len(distinct) <= k:
                    if s[j] in distinct:
                        distinct[s[j]] += 1
                    else:
                        distinct[s[j]] = 1
                else:
                    break
                j += 1
            max_length = max(max_length, j - i - 1)
            print(i,j, max_length)
            while len(distinct) > k:

                distinct[s[i]] -= 1
                if distinct[s[i]] == 0:
                    del distinct[s[i]]
                i += 1
        return max_length


s = "a"
k = 2
x = Solution().lengthOfLongestSubstringKDistinct(s,k)
print(x)
