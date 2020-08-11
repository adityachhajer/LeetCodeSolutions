class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A)<=2:
            return 0
        dp=[0 for _ in range(len(A)+1)]
        ans=0
        for i in range(2,len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
                ans+=dp[i]
        return ans