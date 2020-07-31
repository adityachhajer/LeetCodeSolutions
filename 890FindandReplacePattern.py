class Solution:
    def solve(self,word,pattern):
        m1={}
        m2={}
        a=''
        b=''
        k=0
        for i,j in zip(word,pattern):
            if i not in m1.keys() and j not in m2.keys():
                m1[i]=k
                m2[j]=k
                k+=1
            if i in m1.keys() and j in m2.keys():
                a=a+str(m1[i])
                b=b+str(m2[j])
            else:
                return False
        if a==b:
            return True
        return False
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        l=[]
        for word in words:
            if len(set(word))==len(set(pattern)):
                x=self.solve(word,pattern)
                if x==True:
                    l.append(word)
        return l