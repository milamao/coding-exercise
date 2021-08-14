# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # thoughts:
        # first build an edge map
        # then apply BFS
        edges = {}
        tgt_node = self.get_edges(root, edges, target)  # {node => [node1, node2]}

        if k == 0:
            return [tgt_node.val]

        res = []
        queue = collections.deque()
        queue.append(tgt_node)
        visited = {}  # key is node, value is the distance to target node
        visited[tgt_node] = 0
        while queue:
            node = queue.popleft()
            d = visited[node]
            if d == k:
                res.append(node.val)
            if d > k:
                break
            if node in edges:
                for neighbor in edges[node]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited[neighbor] = d + 1

        return res

    def get_edges(self, root, edges, target):
        left, right = None, None
        if root.left:
            neighbors = edges.get(root, [])
            neighbors.append(root.left)
            edges[root] = neighbors

            neighbors = edges.get(root.left, [])
            neighbors.append(root)
            edges[root.left] = neighbors

            left = self.get_edges(root.left, edges, target)

        if root.right:
            neighbors = edges.get(root, [])
            neighbors.append(root.right)
            edges[root] = neighbors

            neighbors = edges.get(root.right, [])
            neighbors.append(root)
            edges[root.right] = neighbors

            right = self.get_edges(root.right, edges, target)

        if root == target:
            return root
        if left:
            return left
        return right