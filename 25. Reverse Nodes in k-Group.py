"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# With constant extra memory. Space complexity: O(1)
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = dummy
        while pre:
            head = pre.next
            count = k
            while count != 0 and tail:
                tail = tail.next
                count -= 1
            if not tail:
                break
            head = pre.next
            while pre.next != tail:
                curr = pre.next
                pre.next = curr.next
                curr.next = tail.next
                tail.next = curr
            pre = head
            tail = head
        return dummy.next

# Using extra memory. Space complexity: O(k)
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        node = head
        curr = dummy
        stack = []
        while node:
            while node and len(stack) < k:
                stack.append(node)
                node = node.next
            if len(stack) == k:
                while stack:
                    curr.next = stack.pop()
                    curr = curr.next
        curr.next = None
        if stack:
            curr.next = stack.pop(0)
        return dummy.next


