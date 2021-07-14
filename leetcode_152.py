class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = curr_min = max_overall = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num == 0:
                curr_max = curr_min = 0
            else:
                new_max = max(curr_max * num, curr_min * num, num)
                new_min = min(curr_max * num, curr_min * num, num)
                curr_max, curr_min = new_max, new_min
            max_overall = max(max_overall, curr_max)

        return max_overall