"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


#This is copied solution from LeetCode discussions
# the idea is if you switch head, the possible difference between length would be countered.
# On the second traversal, they either hit or miss.
# if they meet, pa or pb would be the node we are looking for,
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            A, B = headA, headB
            while A!=B:
                A = A.next if A else headB
                B = B.next if B else headA
            return A

"""
This was my solution to the problem, but got time limit exceeded error

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA == headB:
            return headA

        rootA = headA
        rootB = headB
        countA = countB = 0
        while headA:
            countA += 1
            headA = headA.next

        while headB:
            countB += 1
            headB = headB.next

        heightDiff = countA - countB

        if heightDiff > 0:
            while heightDiff > 0:
                rootA = rootA.next
                heightDiff -= 1
        else:
            while heightDiff < 0:
                rootB = rootB.next
                heightDiff += 1

        while rootA and rootB:
            if rootA == rootB:
                return rootA

        return None
"""


