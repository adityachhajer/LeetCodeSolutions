class Solution:
    def trap(self, height: List[int]) -> int:
        l = []
        ll = 0
        r = []
        rr = 0
        n = len(height)
        for i in range(len(height)):
            ll = max(ll, height[i])
            l.append(ll)
            rr = max(rr, height[n - i - 1])
            r.append(rr)
        r.reverse()
        c = 0
        for i in range(len(height)):
            c += (min(l[i], r[i]) - height[i])
        return c
