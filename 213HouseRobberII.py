# Not so efficient
# def solve(nums,n,x):
#     if n-1<0:
#         return 0
#     if n-1==0:
#         return nums[n-1]
#     if x[n]!=0:
#         return x[n]
#     else:
#         x[n]=max(nums[n - 1] + solve(nums, n - 2,x), solve(nums, n-1,x ))
#         return x[n]
# if __name__ == '__main__':
#     nums=[1,2,3,1]
#     x = [0 for i in range(len(nums))]
#     p= solve(nums[1:],len(nums)-1,x)
#     x = [0 for i in range(len(nums))]
#     t=solve(nums[0:len(nums)-1],len(nums)-1,x)
#     print(max(t,p))
# ----------------------------------------------------------------------------------------------------------------------
#  efficient
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def house_robber(nums):
#             dp = [0] * len(nums)
#             dp[0] = nums[0]
#             dp[1] = max(nums[0], nums[1])
#             for i in range(2,len(nums)):
#                 dp[i] = max(dp[i-1], nums[i]+dp[i-2])
#             return max(dp[-1], dp[-2])
#
#         if len(nums) <=2 : return max([0] + nums)
#         return max( house_robber(nums[1:]), house_robber(nums[:-1]) )