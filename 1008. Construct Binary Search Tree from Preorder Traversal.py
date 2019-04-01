"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)



Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]



Note:

1 <= preorder.length <= 100
The values of preorder are distinct.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        # Fllowing code is if the input is the root of a tree and we want to do preorder traversal
        # root = None
        # queue = [preorder]
        # while queue:
        #     node = queue.pop()
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        #     if root is None:
        #         root = TreeNode(node.val)
        #     else:
        #         self.insertBST(root, node.val)

        root = TreeNode(preorder[0])
        for val in preorder[1:]:
            self.insertBST(root, val)

        return root

    def insertBST(self, root, val):

        if val <= root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertBST(root.left, val)
        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertBST(root.right, val)

