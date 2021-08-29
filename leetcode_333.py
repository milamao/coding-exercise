# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Solution 2: recursion. check if each subtree is a valid BST.
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_size = 0
        self.check_tree(root)
        return self.max_size

    def check_tree(self, root):
        if not root:
            return True, None, None, 0

        if not root.left and not root.right:
            self.max_size = max(self.max_size, 1)
            return True, root.val, root.val, 1

        is_left_valid, left_min, left_max, left_num_nodes = self.check_tree(root.left)
        if is_left_valid:
            self.max_size = max(self.max_size, left_num_nodes)

        is_right_valid, right_min, right_max, right_num_nodes = self.check_tree(root.right)
        if is_right_valid:
            self.max_size = max(self.max_size, right_num_nodes)

        if self.is_valid_bst(is_left_valid, is_right_valid, root, left_max, right_min):
            num_nodes = left_num_nodes + 1 + right_num_nodes
            self.max_size = max(self.max_size, num_nodes)
            if not left_min:
                left_min = root.val
            if not right_max:
                right_max = root.val
            return True, left_min, right_max, num_nodes

        return False, None, None, 0

    def is_valid_bst(self, is_left_valid, is_right_valid, root, left_max, right_min):
        if not (is_left_valid and is_right_valid):
            return False
        if root.left and root.val <= root.left.val:
            return False
        if root.right and root.val >= root.right.val:
            return False
        if left_max is not None and root.val <= left_max:
            return False
        if right_min is not None and root.val >= right_min:
            return False
        return True

    # Solution 1: inorder traversal + check if each subtree is a valid subtree
    def largestBSTSubtreeV1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        vals = []
        dict = {}  # {<node> => <index_in_vals>}
        self.inorder(root, vals, dict)  # O(n)

        self.max_size = 1
        self.is_BST(vals, dict, 0, len(vals) - 1, root)  # O(nlog(n))
        return self.max_size

    def is_BST(self, vals, dict, start, end, root):
        if start > end or not root:
            return

        count = 0
        is_valid = True
        vals2 = list(vals)  # O(n)
        for i in range(start, end):
            if vals2[i] == '#':
                count += 1
                continue
            if vals2[i + 1] == '#':
                count += 1
                vals2[i + 1] = vals2[i]
                continue
            if vals2[i] >= vals2[i + 1]:
                is_valid = False
                break

        if is_valid:
            # the whole list is in order
            self.max_size = max(self.max_size, end - start + 1 - count)
            return

        pos = dict[root]
        self.is_BST(vals, dict, start, pos - 1, root.left)
        self.is_BST(vals, dict, pos + 1, end, root.right)

    def inorder(self, root, vals, dict):
        # this is a leaf node
        if not root.left and not root.right:
            vals.append(root.val)
            dict[root] = len(vals) - 1
            return

        # this is not a leaf node
        if root.left:
            self.inorder(root.left, vals, dict)
        else:
            vals.append('#')

        vals.append(root.val)
        dict[root] = len(vals) - 1

        if root.right:
            self.inorder(root.right, vals, dict)
        else:
            vals.append('#')