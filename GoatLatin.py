class Solution:
    def toGoatLatin(self, S: str) -> str:
        l=list(S.split(' '))
        vow=['a','e','i','o','u','A','E','I','O','U']
        ans=[]
        x='a'
        for i in l:
            if i[0] in vow:
                s=i+'ma'+x
                ans.append(s)
            else:
                s=i[1:]+i[0]+'ma'+x
                ans.append(s)
            x=x+'a'
        return ' '.join(ans)
