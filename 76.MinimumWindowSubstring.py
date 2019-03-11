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


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        anchor = end = 0
        counter = len(t)
        result = len(s) + 1
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
        return "" if result == len(s) + 1 else s[head:head + result]


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s,t))

