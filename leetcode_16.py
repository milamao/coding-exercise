class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()  # O(nlogn)

        closest_sum = float('INF')
        min_diff = float('INF')

        for i in range(len(nums)):
            sum_of_two = self.two_sum(nums, i + 1, target - nums[i])
            if abs(nums[i] + sum_of_two - target) < min_diff:
                min_diff = abs(nums[i] + sum_of_two - target)
                closest_sum = nums[i] + sum_of_two
                if min_diff == 0:
                    break

        return closest_sum

    def two_sum(self, nums, start, target):
        left, right = start, len(nums) - 1
        closest_sum = float('INF')
        min_diff = float('INF')
        while left < right:
            curr_sum = nums[left] + nums[right]
            if abs(curr_sum - target) < min_diff:
                closest_sum = curr_sum
                min_diff = abs(curr_sum - target)
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                break

        return closest_sum