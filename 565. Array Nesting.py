class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        l = [set() for _ in range(len(nums))]
        ans = float('-inf')
        vis = [False] * len(nums)
        for i in range(len(nums)):
            j = i
            while not vis[j]:
                l[i].add(nums[j])
                vis[j] = True
                j = nums[j]

            ans = max(ans, len(l[i]))
        return ans