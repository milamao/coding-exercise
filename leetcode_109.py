# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 1: use an array
    def sortedListToBSTV1(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return self.build_bst(vals, 0, len(vals) - 1)

    def build_bst(self, vals, start, end):
        if start > end:
            return None

        if start == end:
            return TreeNode(vals[start])

        mid = (start + end) // 2
        root = TreeNode(vals[mid])
        root.left = self.build_bst(vals, start, mid - 1)
        root.right = self.build_bst(vals, mid + 1, end)
        return root

    # Solution 2: O(1) extra space
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        prev, mid = self.find_mid(head)
        prev.next = None

        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root

    def find_mid(self, head):
        prev = ListNode(0, head)
        slow, fast = head, head
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        return prev, slow