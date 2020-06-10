class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0]
        cur_max = nums[0]
        prev_min = nums[0]
        prev_max = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], nums[i] * prev_min, nums[i] * prev_max)
            cur_min = min(nums[i], nums[i] * prev_min, nums[i] * prev_max)
            result = max(result, cur_max)
            prev_max = cur_max
            prev_min = cur_min
        return result

