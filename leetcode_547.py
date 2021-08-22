class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        total = 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and j not in visited:
                    self.explore(isConnected, j, visited)
                    total += 1

        return total

    def explore(self, isConnected, j, visited):
        n = len(isConnected)
        queue = collections.deque()
        queue.append(j)
        visited.add(j)
        while queue:
            city = queue.popleft()
            for i in range(n):
                if isConnected[city][i] and i not in visited:
                    queue.append(i)
                    visited.add(i)