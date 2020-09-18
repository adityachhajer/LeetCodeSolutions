class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y=0,0
        d=0
        dire=[[0,1],[1,0],[0,-1],[-1,0]]
        for i in instructions:
            if i=='G':
                x+=dire[d%4][0]
                y+=dire[d%4][1]
            elif i=='L':
                d-=1
            else:
                d+=1
        return [x,y]==[0,0] or d%4!=0