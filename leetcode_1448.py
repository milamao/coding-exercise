# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # toughts: use recursion to explore all paths
        self.count = 0
        self.traverse(root, root.val)
        return self.count

    def traverse(self, node, max_val):
        if not node:
            return
        if node.val >= max_val:
            self.count += 1
            max_val = node.val
        self.traverse(node.left, max_val)
        self.traverse(node.right, max_val)