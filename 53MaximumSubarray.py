class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = totalsum = nums[0]
        for i in nums[1:]:
            maxsum = max(maxsum + i, i)
            totalsum = max(totalsum, maxsum)
        return totalsum
