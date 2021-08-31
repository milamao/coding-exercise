class Solution:
    DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # Solution 2: DFS. super cool solution.
    # cal areas of islands, group areas by border cell, then try to change each border to 0
    # and see what is the sum of all the adjoining areas
    def largestIsland(self, grid: list[list[int]]) -> int:
        border = defaultdict(set)  # map border cell to area ids: (r,c) : <id, id>
        n = len(grid)
        seen = [[False] * n for _ in range(n)]

        areas = []
        id = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not seen[i][j]:
                    area = self.dfs(seen, grid, i, j, id, border)
                    areas.append(area)
                    id += 1

        if border:
            return max(1 + sum(areas[id] for id in ids) for ids in border.values())
        else:
            return n ** 2 if grid[0][0] == 1 else 1

    def dfs(self, seen, grid, r, c, id, border):
        seen[r][c] = True
        area = 1
        for dx, dy in self.DIRECTIONS:
            x, y = r + dx, c + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid):
                if grid[x][y] == 0:
                    border[(x, y)].add(id)
                elif grid[x][y] == 1 and not seen[x][y]:
                    area += self.dfs(seen, grid, x, y, id, border)
        return area