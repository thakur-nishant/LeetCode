"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
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

