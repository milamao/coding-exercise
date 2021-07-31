class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        # Write your code here
        if n == 1:
            return 0
        if n == 2:
            return roads[0][2]
        next_cities = self.get_next_cities(roads) # <city> => (<city>, <cost>)
        self.min_cost = float('INF')
        curr_cost = 0
        curr_city = 1
        visited = set()
        visited.add(curr_city)
        self.dfs(next_cities, visited, curr_city, curr_cost, n)
        return self.min_cost

    def dfs(self, next_cities, visited, curr_city, curr_cost, n):
        if curr_cost >= self.min_cost:
            return
        if len(visited) == n:
            self.min_cost = curr_cost
            return
        if curr_city not in next_cities: # there is no path from this city to another city
            return
        for next_city, cost in next_cities[curr_city]:
            if next_city in visited:
                continue
            visited.add(next_city)
            self.dfs(next_cities, visited, next_city, curr_cost + cost, n)
            visited.remove(next_city)

    def get_next_cities(self, roads):
        next_cities = {}
        for this_city, next_city, cost in roads:
            entry = next_cities.get(this_city, [])
            entry.append((next_city, cost))
            next_cities[this_city] = entry

            entry = next_cities.get(next_city, [])
            entry.append((this_city, cost))
            next_cities[next_city] = entry

        return next_cities