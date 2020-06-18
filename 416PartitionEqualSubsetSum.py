class Solution:
    def solve(self,nums):
        if sum(nums)%2!=0:
            return False
        total = sum(nums) // 2
        t = [[False for _ in range(total + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums)+1):
            t[i][0]=True
        for i in range(1,len(nums)+1):
            for j in range(1,total+1):
                if nums[i-1]>j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i-1][j-nums[i-1]] or t[i-1][j]
        return t[-1][-1]
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        return self.solve(nums)







