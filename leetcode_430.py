"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    """
    Solution: follow child recursively, and then follow next pointer
    """

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        if not head.next and not head.child:
            return head

        self.connect(head)

        return head

    def connect(self, head):
        if not head.next and not head.child:
            return head, head

        curr = head
        next_node = head.next  # !!!
        if head.child:
            hd, tail = self.connect(head.child)
            curr.next = hd
            hd.prev = curr  # !!!
            curr = tail
            head.child = None

        if next_node:
            hd, tail = self.connect(next_node)
            curr.next = hd
            hd.prev = curr  # !!!
            curr = tail

        return head, curr  # !!!