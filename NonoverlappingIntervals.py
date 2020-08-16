class Solution:
    def eraseOverlapIntervals(self, intervals):
        ans=sorted(intervals,key = lambda sub:(sub[1]-sub[0]))
        l=[[False, False] for _ in range(1000)]
        c=0
        for i in ans:
            if l[i[0]][0] == False and l[i[1]][1]==False:
                l[i[0]][0]=True
                l[i[0]][1]=True
            else:
                c=c+1
        return c


if __name__ == '__main__':
    s=Solution()
    intervals= [[1,2],[2,3]]
    print(s.eraseOverlapIntervals(intervals))


