# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # level order traversal
        if not root:
            return ""
        levels = []
        queue = collections.deque([root])
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if not node:
                    level.append('N')
                else:
                    level.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
            levels.append(",".join(level))

        return "#".join(levels)
        # [1,2,3,null,null]
        # "1#2,3#N,N,4,5"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        levels = []
        for level in data.split("#"):
            levels.append(level.split(","))  # [[1], [2,3], [N,N,4,5]]

        root = TreeNode(int(levels[0][0]))
        queue = collections.deque([root])
        for i in range(1, len(levels)):
            while queue and levels[i]:
                node = queue.popleft()
                # left child
                val = levels[i].pop(0)
                if val != 'N':
                    node.left = TreeNode(int(val))
                    queue.append(node.left)
                if levels[i]:
                    # right child
                    val = levels[i].pop(0)
                    if val != 'N':
                        node.right = TreeNode(int(val))
                        queue.append(node.right)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))