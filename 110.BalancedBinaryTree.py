"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.maxDepthAndBalance(root)[1]

    def maxDepthAndBalance(self, root):
        if root is None:
            return 1, True

        lnode = root.left
        rnode = root.right

        lheight, lbal = self.maxDepthAndBalance(lnode)
        rheight, rbal = self.maxDepthAndBalance(rnode)

        curBal = True if abs(lheight - rheight) <= 1 else False

        return max(lheight, rheight) + 1, curBal and lbal and rbal

