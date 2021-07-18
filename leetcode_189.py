class Solution(object):
    # Solution 1: O(n) space
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return

        k %= n
        new_nums = nums[n - k:] + nums[0:n - k]
        for i in range(n):
            nums[i] = new_nums[i]
        return

    # Solution 2: O(1) space but TLE
    def rotate2(self, nums, k):
        n = len(nums)
        if n == 1:
            return

        k %= n
        for i in range(n - k):
            nums.append(nums.pop(0))

        return

    # Solution 3: 2 pointers (start position and current position)
    def rotate(self, nums, k):
        n = len(nums)
        if n == 1:
            return
        if k % n == 0:
            return

        total = 0
        curr_pos, start_pos = 0, 0
        curr_val = nums[curr_pos]
        temp = None
        while total < n:
            new_pos = (curr_pos + k) % n
            temp = nums[new_pos]
            nums[new_pos] = curr_val
            total += 1
            if total >= n:
                break
            curr_pos = new_pos
            curr_val = temp
            if curr_pos == start_pos:
                curr_pos += 1
                start_pos += 1
                curr_val = nums[curr_pos]