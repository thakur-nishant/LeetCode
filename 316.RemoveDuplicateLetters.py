"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"

"""


class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        stack = []
        for i in range(len(s)):
            print(stack)
            if s[i] not in dic:
                dic[s[i]] = 1
                stack.append(s[i])
            else:
                if ord(stack[len(stack) - 1]) < ord(s[i]) and stack[stack.index(s[i])] > stack[stack.index(s[i]) + 1]:
                    stack.pop(stack.index(s[i]))
                    stack.append(s[i])
                elif stack.index(s[i]) == 0 and ord(s[0]) > ord(s[1]) :
                    stack.append(stack.pop(0))

        result = ''.join(stack)
        return result

s = "cbacdcbc"

x = Solution().removeDuplicateLetters(s)
print(x)
