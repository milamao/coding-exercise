class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1

        if n == 2:
            return 2

        numUniqueTrees = [1] * (n + 1)
        # base cases
        numUniqueTrees[0] = 1
        numUniqueTrees[1] = 1
        numUniqueTrees[2] = 2

        # Given a sequence 1 ... n, we pick a number i out of the sequence as the root,
        # then the number of unique BST with the specified root is the *cartesian product*
        # of the number of BST for its left and right subtrees
        for i in range(3, n + 1):
            total = 0
            for j in range(0, i):
                total += numUniqueTrees[j] * numUniqueTrees[i - 1 - j]
            numUniqueTrees[i] = total

        return numUniqueTrees[n]