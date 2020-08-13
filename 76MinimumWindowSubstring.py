import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        S=s
        T=t
        a=collections.Counter(T)
        i,j,l,r=0,0,0,0
        missing=len(T)
        while r<len(S):
            if a[S[r]]>0:
                missing-=1
            a[S[r]]-=1
            r+=1
            while missing==0:
                if j==0 or r-l<j-i:
                    i,j=l,r
                a[S[l]]+=1
                if a[S[l]]>0: missing+=1
                l+=1


        return S[i:j]