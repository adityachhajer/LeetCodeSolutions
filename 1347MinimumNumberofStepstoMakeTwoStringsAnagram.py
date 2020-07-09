class Solution:
    def minSteps(self, s: str, t: str) -> int:
        di={}
        for i in s:
            if i not in di.keys():
                di[i]=1
            else:
                di[i]+=1
        c=0
        for i in t:
            if i in di.keys():
                if di[i]!=0:
                    di[i] -= 1
                else:
                    c=c+1
            else:
                c=c+1
        return c