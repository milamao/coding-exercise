class Solution(object):

    # Solution 2: dict. O(n)
    def maxSubArrayLen(self, nums, k):
        max_len = 0
        sums = {0: -1}  # sum => index
        rolling_sum = 0
        for i, num in enumerate(nums):
            rolling_sum += num
            if rolling_sum - k in sums:
                max_len = max(max_len, i - sums[rolling_sum - k])
            if rolling_sum not in sums:
                sums[rolling_sum] = i

        return max_len

    # Solution 1: prefix sum. time limit exceeded. O(n^2)
    '''
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        sums = [] # prefix sum
        sums.append(nums[0])
        for i in range(1, n):
            sums.append(sums[-1] + nums[i])

        for length in range(n, -1, -1):
            for i in range(0, n - length + 1):
                if i == 0 and sums[i + length - 1] == k:
                    return length
                if i > 0 and sums[i + length - 1] - sums[i - 1] == k:
                    return length

        return 0
    '''