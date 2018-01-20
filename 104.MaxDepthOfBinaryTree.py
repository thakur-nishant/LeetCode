"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        lnode = root.left
        rnode = root.right

        lheight = 1 + self.maxDepth(lnode)
        rheight = 1 + self.maxDepth(rnode)

        return max(lheight, rheight)

