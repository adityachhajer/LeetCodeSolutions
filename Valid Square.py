import math
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        l=[]
        l.append(p1)
        l.append(p2)
        l.append(p3)
        l.append(p4)
        t=[]
        a=list(l)
        for i in range(len(l)):
            x1=l[i][0]
            y1=l[i][1]
            for j in range(len(l)):
                if i!=j:
                    x2 = l[j][0]
                    y2 = l[j][1]
                    ans=math.sqrt((x2-x1)**2 + (y2-y1)**2)
                    if ans not in t:
                        t.append(ans)
                        if (len(t))>2 or (x1==x2 and y1==y2):
                            return False
        return True
