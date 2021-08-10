class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = collections.deque()
        root = float('-INF')

        for i in range(len(preorder)):
            if not stack or stack[-1] > preorder[i]:
                if preorder[i] < root:
                    return False
                stack.append(preorder[i])
            else:
                while stack and stack[-1] < preorder[i]:
                    root = stack[-1]
                    stack.pop()
                stack.append(preorder[i])

        return True

    """
    Solution explanation:

    A preorder sequence consists of nested structure of {Node, Left subtree, Right Subtree} triplet.

    To verify a preorder sequence, we only need to verify if the sequence has the characteristics of BST, 
    which is, for every given node,
        it's the lower bound to its right subtree,
        it's the upper bound to its left subtree.
    We use the first characteristic to implement the solution:

    use a "lower" to keep track of the current lower bound. 
    Initially lower = INT_MIN, which means no lower bound at first.

    use a stack to store cadidates of next lower bound. stack would be kept in decreasing order.

    when looping through the sequence, preorder[i] should be greater than "lower", otherwise return false.

    If preorder[i] is greater than the stack top, it indicates preorder[i] is the first node of a right subtree, 
    and we have to update "lower" to its parent node for validating the rest of the nodes in this right subtree.
    We update "lower" when removing stack top.
    For each removal operation, it's like moving up to upper level in BST, when the stack top is greater than preorder[i], 
    the last removed item is its parent node.

    Push preorder[i] into stack as it could be a parent node for nodes that haven't been visited yet.

    """