"""

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = self.getMap(s)
        dict2 = self.getMap(t)

        if dict1 == dict2:
            return True
        else:
            return False

    def getMap(self, st):
        temp = {}
        for i in st:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1

        return temp

