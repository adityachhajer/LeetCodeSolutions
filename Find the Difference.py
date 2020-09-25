class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        t=sorted(t)
        a=len(s)
        i=0
        while i<a:
            if t[i]!=s[i]:
                return t[i]
            i+=1
        return t[i]