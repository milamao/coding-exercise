class Solution:
    def countArrangement(self, n: int) -> int:
        # thoughts
        # arrange the numbers in different orders (permutation)
        # check if every arrangement is a "beautiful arrangement"
        self.count = 0
        self.dfs(n, [0], set())
        return self.count

    def dfs(self, n, perm, visited):
        l = len(perm)
        if l > 1:
            if perm[-1] % (l - 1) != 0 and (l - 1) % perm[-1] != 0:
                return
        if l == n + 1:
            self.count += 1
            return
        for i in range(1, n + 1):
            if i in visited:
                continue
            visited.add(i)
            perm.append(i)
            self.dfs(n, perm, visited)
            perm.pop()
            visited.remove(i)