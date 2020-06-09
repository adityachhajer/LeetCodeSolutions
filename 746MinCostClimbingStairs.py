class Solution:
    def solve(self, cost, n, i, l):
        if i == n - 1:
            l[i] = cost[n - 1]
            return l[i]
        if i >= n:
            return 0
        if l[i] != -1:
            return l[i]
        else:
            l[i] = min(cost[i] + self.solve(cost, n, i + 2, l), cost[i] + self.solve(cost, n, i + 1, l))
            return l[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = [-1 for i in range(len(cost))]
        return min(self.solve(cost, len(cost), 0, l), self.solve(cost, len(cost), 1, l))