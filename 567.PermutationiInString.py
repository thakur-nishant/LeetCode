"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False
        map_s1 = self.mapChars(s1)
        map_s2 = self.mapChars(s2[:len_s1])
        if map_s1 == map_s2:
            return True
        for i in range(1, len_s2 - len_s1 + 1):
            map_s2[s2[i - 1]] -= 1
            map_s2[s2[i + len_s1 -1]] += 1
            # print(s2[i:i+len_s1])
            if map_s1 == map_s2:
                return True

        return False

    def mapChars(self, s):
        my_map = {}
        for i in range(26):
            my_map[chr(97 + i)] = 0
        for c in s:
            my_map[c] += 1
        return my_map


s1 = "ab"
s2 = "eidboaoooba"
x = Solution().checkInclusion(s1,s2)
print(x)