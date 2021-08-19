# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return self.array_to_tree(0, len(preorder) - 1, preorder, inorder_index_map)

    def array_to_tree(self, left, right, preorder, inorder_index_map):
        if left > right:
            return None

        root_value = preorder.pop(0)
        root = TreeNode(root_value)

        root.left = self.array_to_tree(left, inorder_index_map[root_value] - 1, preorder, inorder_index_map)
        root.right = self.array_to_tree(inorder_index_map[root_value] + 1, right, preorder, inorder_index_map)

        return root