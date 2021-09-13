# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []

        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        res = [0] * length

        cur = head
        index = 0
        while cur:
            while stack and stack[-1][1] < cur.val:
                item = stack.pop()
                res[item[0]] = cur.val

            stack.append((index, cur.val))
            cur = cur.next
            index += 1

        return res