# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_map = {}
        for i in range(len(postorder)):
            postorder_map[postorder[i]] = i

        return self.build(0, len(preorder) - 1, preorder, postorder_map)

    def build(self, start, end, preorder, postorder_map):
        if start > end:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        if start == end:
            return root

        left_val = preorder[0]
        root.left = self.build(start, postorder_map[left_val], preorder, postorder_map)
        root.right = self.build(postorder_map[left_val] + 1, end - 1, preorder, postorder_map)
        return root