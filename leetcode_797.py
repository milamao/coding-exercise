class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        if not n:
            return []
        paths = []
        self.dfs(graph, 0, n - 1, [0], paths)
        return paths

    def dfs(self, graph, curr, target, path, paths):
        if curr == target:  # true if reached destination
            paths.append(list(path))
            return

        for next in graph[curr]:
            path.append(next)
            self.dfs(graph, next, target, path, paths)
            path.pop()