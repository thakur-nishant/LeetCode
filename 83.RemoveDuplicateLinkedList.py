"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lookup = {}
        result = head
        pre = head
        while head:
            if head.val in lookup:
                if head.next is not None:
                    pre.next = head.next
                else:
                    pre.next = None
            else:
                lookup[head.val] = 1
                pre = head

            head = head.next

        return result

