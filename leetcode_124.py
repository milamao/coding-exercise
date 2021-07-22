# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float('-INF')
        self.maxGain(root)
        return self.maxSum

    def maxGain(self, node):
        if not node:
            return 0

        # max sum on the left and right sub-trees of node
        left_gain = max(self.maxGain(node.left), 0)
        right_gain = max(self.maxGain(node.right), 0)

        # the price to start a new path where `node` is a highest node
        price_newpath = node.val + left_gain + right_gain

        # update max_sum if it's better to start a new path
        self.maxSum = max(self.maxSum, price_newpath)

        # for recursion :
        # return the max gain if continue the same path
        return node.val + max(left_gain, right_gain)