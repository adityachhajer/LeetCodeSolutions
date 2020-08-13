class Solution:
    def allfactors(self,n):
        l=[-1 for _ in range(n+1)]
        l[0]=0
        l[1]=1
        for i in range(2,n+1):
            if l[i]==-1:
                for j in range(i,n+1,i):
                    if l[j]==-1:
                        l[j]=i
        ans=[]
        while n>1:
            ans.append(l[n])
            n = n // l[n]
        return ans

    def minSteps(self, n: int) -> int:
        return sum(self.allfactors(n))