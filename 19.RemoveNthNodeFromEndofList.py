"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        rm_index = length - n
        if rm_index == 0:
            if length == 1:
                return None
            else:
                head = head.next
                return head
        index = 0
        pre = None
        node = head
        while index != rm_index:
            index += 1
            pre = node
            node = node.next

        pre.next = node.next

        return head



