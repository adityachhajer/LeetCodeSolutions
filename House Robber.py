class Solution:
    def solve(self, nums, ans, i, l):
        if i < 0:
            return 0
        if l[i] != -1:
            return l[i]
        else:
            l[i] = max(self.solve(nums, ans, i - 1, l), nums[i] + self.solve(nums, ans, i - 2, l))
            return l[i]

    def rob(self, nums: List[int]) -> int:
        ans = 0
        l = [-1] * (len(nums) + 1)
        return self.solve(nums, ans, len(nums) - 1, l)

