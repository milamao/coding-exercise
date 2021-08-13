# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution 2: DFS
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        rightside = []
        self.helper(root, 0, rightside)
        return rightside

    def helper(self, node, level, rightside):
        if level == len(rightside):
            rightside.append(node.val)

        for child in [node.right, node.left]:
            if child:
                self.helper(child, level + 1, rightside)

    # Solution 1: level order traversal
    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        # thoughts: level order travesal, get the last node at each level
        vals = []
        self.levelorder(root, vals)
        return vals

    def levelorder(self, root, vals):
        queue = collections.deque()
        queue.append(root)
        queue.append('#')
        level = []
        while queue:
            node = queue.popleft()
            if not node:
                continue
            if node == '#':
                if level:
                    vals.append(level[-1])
                level = []
                if queue:
                    queue.append('#')
                continue
            level.append(node.val)
            queue.append(node.left)
            queue.append(node.right)