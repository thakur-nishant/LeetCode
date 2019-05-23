"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
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
            if level % 2 == 0:
                result.append(record[level])
            else:
                result.append(record[level][::-1])

        return result

