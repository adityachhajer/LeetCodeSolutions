class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        summ=S
        a=sum(nums)
        s1=(a+summ)//2
        x=len(nums)
        t=[[0 for _ in range(s1+1)]for _ in range(x+1)]
        for i in range(x+1):
            t[i][0]=1
        for i in range(1,x+1):
            for j in range(1,s1+1):
                if nums[i-1]>j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j] = t[i - 1][j]+t[i-1][j-nums[i-1]]
        return t[-1][-1]