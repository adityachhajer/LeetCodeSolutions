class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=''
        for i in range(len(s)):
            if i==0 or i==len(s)-1:
                if s[i].isalnum() or s[i]==' ' or s[i]=='':
                    x = x + s[i].lower()
            else:
                if s[i].isalnum():
                    x=x+s[i].lower()
        i=0
        j=len(x)-1
        while i<=j:
            if x[i]==x[j]:
                i += 1
                j -= 1
            else:
                return False
        return True