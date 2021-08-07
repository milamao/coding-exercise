class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n or k * 9 < n:
            return []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        paths = []
        self.dfs(nums, 0, k, n, [], paths)
        return paths

    def dfs(self, nums, start, k, n, path, paths):
        if k == 0:
            if n == 0:
                paths.append(list(path))
            return
        if n < 0:
            return
        if start >= n:
            return

        for i in range(start, 9):
            path.append(nums[i])
            self.dfs(nums, i + 1, k - 1, n - nums[i], path, paths)
            path.pop()