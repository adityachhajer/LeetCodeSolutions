class Solution:
    def solve(self,open,closed,s,l):
        if open==0 and closed==0:
            l.append(s)
            return
        elif open==0 and closed!=0:
            s=s+')'
            return self.solve(open, closed-1, s, l)
        elif open==closed:
            s=s+'('
            return self.solve(open- 1, closed , s, l)
        else:
            self.solve(open- 1, closed , s+'(', l)
            self.solve(open, closed-1 , s+')', l)

    def generateParenthesis(self, n: int) -> List[str]:
        open=n
        closed=n
        s=''
        l=[]
        self.solve(open,closed,s,l)
        return l