class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < k:
            return False

        if k == 1:
            return True

        total = sum(nums)
        if total % k != 0:
            return False

        avg = total // k
        visited = set()
        return self.dfs(nums, visited, 0, k, avg, 0)

    def dfs(self, nums, visited, start, k, goal, sum):
        if k == 1:
            # at this point the remaining value is
            # org_sum - goal * (k-1) = goal * k - goal * (k-1) = goal
            return True

        if sum == goal:
            return self.dfs(nums, visited, 0, k - 1, goal, 0);

        for i in range(start, len(nums)):
            if i in visited:
                continue
            visited.add(i)
            if self.dfs(nums, visited, i + 1, k, goal, sum + nums[i]):
                return True
            visited.remove(i)

        return False