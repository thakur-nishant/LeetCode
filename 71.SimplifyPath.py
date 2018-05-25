"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        for i in path.split('/'):
            if i:
                stack.append(i)

        new_path = ""
        for f in stack:
            if f == '.':
                pass
            elif f == '..':
                index = new_path[:-1].rfind('/')
                new_path = new_path[:index]
            else:
                new_path += '/' + f
        if not new_path:
            new_path = "/"

        return new_path
