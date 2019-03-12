"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next

        carry = 0
        node = ListNode(0)
        while num1 or num2:
            val = carry
            if num1:
                val += num1.pop()
            if num2:
                val += num2.pop()
            node.val = val % 10
            carry = val // 10
            next_node = ListNode(0)
            next_node.next = node
            node = next_node
        if carry:
            node.val = carry
            return node
        return node.next

