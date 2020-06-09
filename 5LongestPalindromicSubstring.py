# ask
class Solution:
    def longestPalindrome(self, s: str) -> str:
        p=''
        i=0
        while i+len(p)<len(s):
            j=s.rfind(s[i])
            while j-i+1>len(p):
                x=s[i:j+1]
                y=x[::-1]
                if x==y:
                    p=x
                    break
                else:
                    j=s.rfind(s[i],i,j)
            i=i+1
        return p
