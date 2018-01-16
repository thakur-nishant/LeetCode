"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        flag1 = True if p is not None else False
        flag2 = True if q is not None else False

        if p == q:
            return True

        if flag1 and flag2:
            if p.val == q.val:
                # Check for the left child
                p1 = p.left
                q1 = q.left
                cflag1 = self.isSameTree(p1, q1)

                # Check for the right child
                p2 = p.right
                q2 = q.right
                cflag2 = self.isSameTree(p2, q2)

                return cflag1 and cflag2
            else:
                return False

        else:
            return False

