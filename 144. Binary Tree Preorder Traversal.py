"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# recursive solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.recurse(root, result)
        return result

    def recurse(self, root, result):
        if not root:
            return

        result.append(root.val)
        self.recurse(root.left, result)
        self.recurse(root.right, result)


# Iterative

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        curr = root

        while True:
            if curr:
                stack.append(curr)
                result.append(curr.val)
                curr = curr.left
            else:
                if stack:
                    curr = stack.pop()
                    curr = curr.right

                else:
                    break

        return result

