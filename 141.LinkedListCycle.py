"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        if not head.next:
            return False

        p1 = head
        p2 = head.next

        while p1 != p2 and p1 and p2:
            if p2.next:
                p1 = p1.next
                p2 = p2.next.next
            else:
                break

        if p1 == p2:
            return True
        return False

