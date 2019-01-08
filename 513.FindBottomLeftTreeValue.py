"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [root.val]
        rlevel = [0]
        self.recursiveSearch(root, result, rlevel, 0)
        # print(result)
        return result[-1]

    def recursiveSearch(self, root, result, rlevel, currlevel):
        if root is None:
            return

        if root.left and currlevel + 1 > rlevel[-1]:
            rlevel.append(currlevel + 1)
            # print(rlevel, currlevel, root.left.val)
            result.append(root.left.val)
        elif root.right and currlevel + 1 > rlevel[-1]:
            rlevel.append(currlevel + 1)
            result.append(root.right.val)

        self.recursiveSearch(root.left, result, rlevel, currlevel + 1)
        self.recursiveSearch(root.right, result, rlevel, currlevel + 1)


