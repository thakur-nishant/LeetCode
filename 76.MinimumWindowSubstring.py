"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

"""
import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start = end = 0
        min_length = len(s) + 1
        counter = len(t)
        log = {}

        for c in t:
            if c in log:
                log[c] += 1
            else:
                log[c] = 1
        while end < len(s):
            if s[end] in log:
                log[s[end]] -= 1
                if log[s[end]] >= 0:
                    counter -= 1
            end += 1

            while counter == 0:
                if (end - start < min_length):
                    min_length = end - start
                    head = start
                if s[start] in log:
                    log[s[start]] += 1
                    if log[s[start]] > 0:
                        counter += 1
                start += 1
        return s[head:head + min_length] if min_length != len(s) + 1 else ""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        anchor = end = 0
        result, counter = len(s) + 1, len(t)
        t_count = collections.Counter(t)
        while end < len(s):
            if s[end] in t_count:
                if t_count[s[end]] > 0:
                    counter -= 1
                t_count[s[end]] -= 1
            end += 1
            while counter == 0:
                if end - anchor < result:
                    result = end - anchor
                    head = anchor
                if s[anchor] in t_count:
                    if t_count[s[anchor]] == 0:
                        counter += 1
                    t_count[s[anchor]] += 1
                anchor += 1
        return "" if result == len(s) + 1 else s[head: head + result]


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s,t))

