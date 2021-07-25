class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return -1

        start, end = 0, len(nums) - 1
        while start + 2 < end:
            mid = (start + end) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid + 1] == nums[mid + 2]:  # the single number is from start to mid
                end = mid
            else:
                start = mid

        if nums[start] == nums[start + 1]:
            return nums[start + 2]
        return nums[start]