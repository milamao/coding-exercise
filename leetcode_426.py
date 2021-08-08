"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    # Solution 2: in-place, faster than 8% submission
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        stack = collections.deque()
        node = root
        while node:
            stack.append(node)
            node = node.left

        head, tail, prev = None, None, None

        while stack:  # O(n)
            curr = stack.pop()
            if not head:
                head = curr
            tail = curr
            if prev:
                prev.right = curr
                curr.left = prev
            if curr.right:
                node = curr.right
                while node:
                    stack.append(node)
                    node = node.left
            prev = curr

        tail.right = head
        head.left = tail
        return head

    # Solution 1: not in-place
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        vals = []
        self.inorder(root, vals)
        head = TreeNode(vals[0])
        curr = head
        for i in range(1, len(vals)):
            next = TreeNode(vals[i])
            next.left = curr
            curr.right = next
            curr = next
        curr.right = head
        head.left = curr
        return head

    def inorder(self, root, vals):
        if root.left:
            self.inorder(root.left, vals)
        vals.append(root.val)
        if root.right:
            self.inorder(root.right, vals)