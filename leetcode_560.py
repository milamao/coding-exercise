class Solution(object):

    # Solution 2: dict
    def subarraySum(self, nums, k):
        total = 0
        n = len(nums)

        sums = {}  # sum => count
        sums[0] = 1
        value = 0
        for i in range(0, n):
            value += nums[i]
            total += sums.get(value - k, 0)
            sums[value] = sums.get(value, 0) + 1

        return total

    # Solution 1: prefix sum. TLE
    '''
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        n = len(nums)

        # build prefix sum array
        sums = []
        sums.append(nums[0])
        if sums[0] == k:
            total += 1
        for i in range(1, n):
            sums.append(sums[i-1] + nums[i])
            if sums[-1] == k:
                total += 1

        # find continuous subarrays whose sum equals to k
        for i in range(0, n-1):
            for j in range(i+1, n):
                if sums[j] - sums[i] == k:
                    total += 1

        return total
    '''