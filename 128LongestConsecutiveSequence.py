# o(nlogn)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 1
#         c = 1
#         maxx = 0
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1] + 1 or nums[i] == nums[i - 1]:
#                 if nums[i] == nums[i - 1]:
#                     c = c
#                 else:
#
#                     c = c + 1
#             else:
#                 c = 1
#             maxx = max(maxx, c)
#         return maxx


# o(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set()
        for i in nums:
            myset.add(i)
        maxx = 0
        for i in range(0, len(nums)):
            if nums[i] - 1 not in myset:
                j = nums[i]
                while (j in myset):
                    j = j + 1
                maxx = max(maxx, j - nums[i])
        return maxx
