class Solution:
    def solve(self, l, n, ll):
        if n < 0:
            return 0
        if n == 0:
            return l[0]
        if ll[n] != -1:
            return ll[n]
        else:
            ll[n] = max(l[n] + self.solve(l, n - 2, ll), self.solve(l, n - 1, ll))
            return ll[n]

    def rob(self, nums: List[int]) -> int:
        ll = [-1 for _ in range(len(nums) + 1)]
        return self.solve(nums, len(nums) - 1, ll)


