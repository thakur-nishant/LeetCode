"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import sys

from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not any(lists):
            return None
        dummy = curr = ListNode(0)
        q = PriorityQueue()
        for idx, node in enumerate(lists):
            if node: q.put((node.val, idx, node))

        while not q.empty():
            val, idx, curr.next = q.get()
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, idx, curr.next))
        return dummy.next


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return lists
        if len(lists) == 1:
            return lists[0]
        head = ListNode(0)
        current_node = head
        pointer_val = [node.val if node is not None else sys.maxsize for node in lists]

        while True:
            min_val_index = pointer_val.index(min(pointer_val))
            if lists[min_val_index]:
                current_node.next = lists[min_val_index]
                lists[min_val_index] = lists[min_val_index].next
                pointer_val[min_val_index] = lists[min_val_index].val if lists[min_val_index] else sys.maxsize
                current_node = current_node.next
            else:
                break
        head = head.next
        return head




