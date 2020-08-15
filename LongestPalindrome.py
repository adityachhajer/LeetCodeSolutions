class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(set(s))==1:
            return len(s)
        di={}
        for i in s:
            if i not in di.keys():
                di[i]=1
            else:
                di[i]+=1
        c = 0
        a = []
        for i in di.values():
            if i % 2 == 0:
                c=c+i
            else:
                a.append(i)
        a.sort()
        for i in range(len(a)):
            if i==len(a)-1:
                c=c+a[i]
            else:
                c=c+a[i]-1
        return c