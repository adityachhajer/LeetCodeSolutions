class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:
            return []
        ans=[]
        di={}
        i=10
        ns=''
        p=0
        j=len(s)
        while(i<=j):
            ns=s[p:i]
            if ns not in di.keys():
                di[ns]=1
            else:
                di[ns]+=1
            p+=1
            i+=1
        for a,b in di.items():
            if b>1:
                ans.append(a)
        return ans