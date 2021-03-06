"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        node = head
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1:
            node.next = l1

        if l2:
            node.next = l2

        return head.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newList = ListNode(0)

        ret = newList

        while l1 and l2:
            if l1.val < l2.val:
                ret.next = l1
                l1 = l1.next
            else:
                ret.next = l2
                l2 = l2.next
            ret = ret.next

        while l1:
            ret.next = l1
            l1 = l1.next
            ret = ret.next

        while l2:
            ret.next = l2
            l2 = l2.next
            ret = ret.next
        # ret.next = l1 if l1 is not None else l2

        return newList.next
