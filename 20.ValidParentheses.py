"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {
            ')': '(',
            '[': None,
            '{': None,
            '(': None,
            ']': '[',
            '}': '{'
        }
        stack = []
        for b in s:
            if lookup[b] == None:
                stack.append(b)
            else:
                if not stack or stack.pop() != lookup[b]:
                    return False
        if not stack:
            return True
        else:
            return False


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        map_parenthesis = {
            "(": ")",
            "{": "}",
            "[": "]",
            "]" : None,
            "}" : None,
            ")" : None
        }

        stack = [s[0]]
        top = 0
        for p in s[1:]:
            if top >= 0 and p == map_parenthesis[stack[top]]:
                stack.pop()
                top -= 1
            else:
                top += 1
                stack.append(p)
        print(stack)
        if stack:
            return False
        return True


"""
class Solution:
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) > 0:
                    if i == ')' and stack.pop() != '(':
                        return False
                    if i == '}' and stack.pop() != '{':
                        return False
                    if i == ']' and stack.pop() != '[':
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
"""
s = "()[]{}"
x = Solution().isValid(s)
print(x)