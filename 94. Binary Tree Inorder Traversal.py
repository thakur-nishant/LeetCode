"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


#Iterative

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
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
                curr = curr.left
            else:
                if stack:
                    curr = stack.pop()
                    result.append(curr.val)

                    curr = curr.right
                else:
                    break

        return result

# Recursive solution

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.recurse(root, result)

        return result

    def recurse(self, root, result):
        if root is None:
            return
        self.recurse(root.left, result)
        result.append(root.val)
        self.recurse(root.right, result)

