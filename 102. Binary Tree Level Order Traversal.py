"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        record = {}
        queue = [(root, 0)]
        max_level = 0
        while queue:
            node, level = queue.pop(0)
            if node == None:
                continue
            max_level = max(max_level, level)
            if level in record:
                record[level].append(node.val)
            else:
                record[level] = [node.val]
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        result = []
        for level in range(max_level + 1):
            result.append(record[level])

        return result

