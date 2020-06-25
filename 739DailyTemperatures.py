class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans=[0]*len(T)
        l=[]
        for i in range(len(T)-1,-1,-1):
            while l and T[i]>=T[l[-1]]:
                l.pop()
            if l:
                ans[i]=l[-1]-i
            l.append(i)
        return ans