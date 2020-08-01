class Solution:
    def solve(self, lo, t):
        if lo == 1:
            return 0
        if lo in t.keys():
            return t[lo]
        if lo % 2 == 0:
            t[lo] = 1 + self.solve(lo // 2, t)
            return t[lo]
        else:
            t[lo] = 1 + self.solve(((3 * lo) + 1), t)
            return t[lo]

    def getKth(self, lo: int, hi: int, k: int) -> int:
        t = {}
        di = {}
        for i in range(lo, hi + 1):
            x = self.solve(i, t)
            di[i] = x
        sort_orders = sorted(di.items(), key=lambda x: x[1], reverse=False)
        for i in sort_orders:
            k -= 1
            if k == 0:
                return i[0]
