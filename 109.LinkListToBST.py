# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return self.listToBST(nums)

    def listToBST(self, nums):

        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])

        root.left = self.listToBST(nums[:mid])
        root.right = self.listToBST(nums[mid + 1:])

        return root

