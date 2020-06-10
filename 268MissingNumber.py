# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         t = [i for i in range(len(nums) + 1)]
#         for i in nums:
#             if i in t:
#                 t.remove(i)
#         return t[0]

# efficient
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=len(nums)
        for i in range(len(nums)):
            x^=i^nums[i]
        return x