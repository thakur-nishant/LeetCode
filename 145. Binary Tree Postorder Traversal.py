"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Iterative

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
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
                result.insert(0, curr.val)
                curr = curr.right
            else:
                if stack:
                    curr = stack.pop()
                    curr = curr.left
                else:
                    break

        return result



# Recursive

class Solution(object):
    def postorderTraversal(self, root):
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
        self.recurse(root.left, result)
        self.recurse(root.right, result)
        result.append(root.val)


