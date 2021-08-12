# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 2: recursion
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left)

    # Solution 1: level order traversal
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        levels = []
        queue = collections.deque()
        queue.append(root)
        queue.append('#')
        level = []
        while queue:
            node = queue.popleft()
            if node == '#':
                levels.append(level[::])
                level = []
                if queue:
                    queue.append('#')
                continue
            if not node:
                level.append('None')
                continue
            level.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        for level in levels:
            l, r = 0, len(level) - 1
            while l < r:
                if level[l] != level[r]:
                    return False
                l += 1
                r -= 1
        return True