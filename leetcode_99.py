# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 2: use stack to find the 2 out-of-place nodes and swap their values
    def recoverTree(self, root: TreeNode):
        """
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        x = y = pred = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    break
            pred = root
            root = root.right

        x.val, y.val = y.val, x.val

    # Solution 1: use recursions to find the 2 out-of-place values, find their nodes, and then swap
    def recoverTree1(self, root: Optional[TreeNode]) -> None:
        vals = []
        self.inorder(root, vals)

        x, y = self.find_swapper_numbers(vals)

        nodes = {}
        self.find_nodes(root, x, y, nodes)

        nodes[x].val = y
        nodes[y].val = x

    def inorder(self, root, vals):
        if not root:
            return
        self.inorder(root.left, vals)
        vals.append(root.val)
        self.inorder(root.right, vals)

    def find_swapper_numbers(self, vals):
        x, y = None, None
        n = len(vals)
        for i in range(0, n - 1):
            if vals[i] > vals[i + 1]:
                for j in range(n - 1, i, -1):  # start from the back
                    if vals[j] < vals[i]:
                        x, y = vals[i], vals[j]
                        return (x, y)

    def find_nodes(self, root, x, y, nodes):
        if not root:
            return

        if root.val == x:
            nodes[x] = root
        elif root.val == y:
            nodes[y] = root

        if len(nodes) == 2:
            return

        self.find_nodes(root.left, x, y, nodes)
        if len(nodes) == 2:
            return
        self.find_nodes(root.right, x, y, nodes)