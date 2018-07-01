"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        node = head
        if m == n:
            return head
        store = []
        count = 1
        while node and count != n:
            if count == m:
                start_node = node
                while count != n:
                    store.append(node.val)
                    node = node.next
                    count += 1
                store.append(node.val)
            else:
                node = node.next
            count += 1

        while store:
            start_node.val = store.pop()
            start_node = start_node.next

        return head


head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

m = 2
n = 4

x = Solution().reverseBetween(head,m,n)
node = x
while node:
    print(node.val)
    node = node.next
