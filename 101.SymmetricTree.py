"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        lnode = root.left
        rnode = root.right

        if lnode and rnode:
            if lnode.val == rnode.val:
                return self.isChildSymmetric(lnode, rnode)
            else:
                return False
        elif lnode or rnode:
            return False
        else:
            return True

    def isChildSymmetric(self, lnode, rnode):
        lflag = False
        rflag = False

        if lnode.left and rnode.right:
            if lnode.left.val == rnode.right.val:
                lflag = self.isChildSymmetric(lnode.left, rnode.right)
        elif lnode.left or rnode.right:
            lflag = False
        else:
            lflag = True

        if lnode.right and rnode.left:
            if lnode.right.val == rnode.left.val:
                rflag = self.isChildSymmetric(lnode.right, rnode.left)
        elif lnode.right or rnode.left:
            rflag = False
        else:
            rflag = True

        return lflag and rflag

