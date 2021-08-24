# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = 0
        cache = {}
        dummy = ListNode(0, head)
        cache[0] = dummy
        while cur:
            prev += cur.val
            # if cumsum has appeared before, we need to remove nodes in between
            if prev in cache:
                temp = cache[prev].next
                t = prev
                # remove all previous nodes between temp and cur
                while temp != cur:
                    t += temp.val
                    del cache[t]
                    temp = temp.next

                cur = cur.next
                cache[prev].next = cur  # reconnect nodes
            else:  # if cumsum never appeared, store cumsum with node
                cache[prev] = cur
                cur = cur.next

        return dummy.next