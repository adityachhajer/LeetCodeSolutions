class Solution:
    def solve(self,l, costs, i, n,t):
        if i >= n:
            return 0
        if t[i]!=-1:
            return t[i]
        if l[i] == 0:
            t[i]=self.solve(l, costs, i + 1, n,t)
            return t[i]
        else:
            t[i]=min(costs[0] + self.solve(l, costs, i + 1, n,t), costs[1] + self.solve(l, costs, i + 7, n,t),
                   costs[2] + self.solve(l, costs, i + 30, n,t))
            return t[i]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        l = [0] * (days[-1] + 1)
        t=[-1]*(len(l)+1)
        for i in days:
            l[i] = 1
        return  self.solve(l, costs, 0, len(l),t)