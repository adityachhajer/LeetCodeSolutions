class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        atl = []
        atr = []
        i = 0
        l = []
        n = len(heights)
        while i < n:
            if len(l) == 0:
                atl.append(-1)
            else:
                if (l[-1][0] < heights[i]):
                    atl.append(l[-1][1])
                else:
                    while l and l[-1][0] >= heights[i]:
                        l.pop(-1)
                    if (len(l) == 0):
                        atl.append(-1)
                    else:
                        atl.append(l[-1][1])
            l.append([heights[i], i])
            i += 1

        i = len(heights) - 1
        l = []
        n = -1
        while i > n:
            if len(l) == 0:
                atr.append(len(heights))
            else:
                if (l[-1][0] < heights[i]):
                    atr.append(l[-1][1])
                else:
                    while l and l[-1][0] >= heights[i]:
                        l.pop(-1)
                    if (len(l) == 0):
                        atr.append(len(heights))
                    else:
                        atr.append(l[-1][1])
            l.append([heights[i], i])
            i -= 1
        atr.reverse()
        wid = []
        for i in range(len(heights)):
            wid.append((heights[i]) * (atr[i] - atl[i] - 1))

        return (max(wid))