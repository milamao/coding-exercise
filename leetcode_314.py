# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution 2: BFS + group nodes by left degree
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columnTable = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in sorted(columnTable.keys())]

    # Solution 1: recursion + group nodes by left degree
    def verticalOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        # assign a degree to each node, root's left degree is 0
        # if it's left child, d - 1
        # if it's right child, d + 1
        if not root:
            return []

        results = []
        dist_node_map = {}
        self.build_map(root, dist_node_map, 0, 0)  # {<left_degree>: [(node_height, node_value)]}

        keys = list(dist_node_map.keys())
        keys.sort()
        for k in keys:
            # vals are nodes with the same left degree
            vals = dist_node_map.get(k)  # [(node_height, node_value)]
            height_val_map = {}
            res = []
            # sort nodes by height
            for h, v in vals:
                values = height_val_map.get(h, [])
                values.append(v)
                height_val_map[h] = values

            keys2 = list(height_val_map.keys())
            keys2.sort()
            for k2 in keys2:
                for v2 in height_val_map[k2]:
                    res.append(v2)
            results.append(res)

        return results

    def build_map(self, node, dist_node_map, left, h):
        nodes = dist_node_map.get(left, [])
        nodes.append((h, node.val))
        dist_node_map[left] = nodes

        if node.left:
            self.build_map(node.left, dist_node_map, left - 1, h + 1)
        if node.right:
            self.build_map(node.right, dist_node_map, left + 1, h + 1)