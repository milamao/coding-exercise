# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Solution 1: O(n) space, O(nlogn) time
    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # loop though the linked list to get all the values,
        # sort the values and reconstruct a linked list
        if not head:
            return None
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        vals.sort()  # O(nlogn)
        head = ListNode(vals[0])
        tail = head
        for i in range(1, len(vals)):
            tail.next = ListNode(vals[i])
            tail = tail.next
        return head

    # Solution 2: O(n) space, O(nlogn) time
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # count number of nodes
        size, cur = 0, head
        while cur:
            cur = cur.next
            size += 1

        # split the linked list
        size = size // 2
        prev, cur = None, head
        while size:
            prev = cur
            cur = cur.next
            size -= 1
        prev.next = None

        # sort sublists
        n1, n2 = self.sortList(head), self.sortList(cur)

        # merge two sublists
        dummy_head = ListNode()
        cur = dummy_head
        while n1 and n2:
            if n1.val < n2.val:
                cur.next = n1
                n1 = n1.next
            else:
                cur.next = n2
                n2 = n2.next
            cur = cur.next
        cur.next = n1 or n2

        return new_head.next