# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    # Solution 2: dfs, beats 34% submissions by time, 71% submissions by memory
    def findDuplicateSubtrees(self, root):
        ans = []
        dict = {}
        self.dfs(root, dict, ans)
        return ans

    def dfs(self, root, dict, ans):
        if not root:
            return ""

        hash = ""
        if not root.left and not root.right:
            hash = str(root.val)
        else:
            hash = str(root.val) + "$" + self.dfs(root.left, dict, ans) + "$" + self.dfs(root.right, dict, ans)

        count = dict.get(hash, 0)
        if count == 1:
            ans.append(root)
        dict[hash] = count + 1

        return hash

    # Solution 1: beats 5% of submission both in terms of time and memory
    def findDuplicateSubtrees1(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []

        memo = {}
        subtree_dict = {}  # tree_expr => [subtree roots]
        self.get_subtree(root.left, subtree_dict, memo)
        self.get_subtree(root.right, subtree_dict, memo)

        subtrees = []
        for k in subtree_dict:
            if len(subtree_dict[k]) > 1:
                subtrees.append(subtree_dict[k][0])

        return subtrees

    def get_subtree(self, root, subtree_dict, memo):
        if not root:
            return

        if root in memo:
            path = memo[root]
        else:
            path = []
            self.levelorder(root, path)
            memo[root] = path

        tree_expr = ",".join(path)
        nodes = subtree_dict.get(tree_expr, [])
        nodes.append(root)
        subtree_dict[tree_expr] = nodes

        self.get_subtree(root.left, subtree_dict, memo)
        self.get_subtree(root.right, subtree_dict, memo)

    def levelorder(self, root, path):
        if not root:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node:
                path.append('N')
                continue
            path.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
