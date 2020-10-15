class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            return max(dp[-1], dp[-2])

        if len(nums) <= 2: return max([0] + nums)
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))