class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    PACIFIC = 'PACIFIC'
    ATLANTIC = 'ATLANTIC'

    # Solution 1: DFS + memoization
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        res = []
        memo = {'p': {}, 'a': {}}
        for i in range(m):
            for j in range(n):
                if not self.dfs(heights, i, j, set([i, j]), self.PACIFIC, memo):
                    memo['p'][(i, j)] = False
                    continue
                if not self.dfs(heights, i, j, set([i, j]), self.ATLANTIC, memo):
                    memo['a'][(i, j)] = False
                    continue

                res.append((i, j))
                memo['p'][(i, j)] = True
                memo['a'][(i, j)] = True

        return res

    def dfs(self, heights, i, j, visited, ocean, memo):
        if ocean == self.PACIFIC:
            if i == 0 or j == 0:
                return True
            if (i, j) in memo['p']:
                return memo['p'][(i, j)]
        else:
            if i == len(heights) - 1 or j == len(heights[0]) - 1:
                return True
            if (i, j) in memo['a']:
                return memo['a'][(i, j)]

        for di, dj in self.DIRECTIONS:
            ni, nj = i + di, j + dj
            if self.is_valid(heights, ni, nj, visited, heights[i][j]):
                visited.add((ni, nj))
                if self.dfs(heights, ni, nj, visited, ocean, memo):
                    return True

        return False

    def is_valid(self, heights, i, j, visited, from_value):
        if i < 0 or i >= len(heights):
            return False
        if j < 0 or j >= len(heights[0]):
            return False
        if (i, j) in visited:
            return False
        return heights[i][j] <= from_value