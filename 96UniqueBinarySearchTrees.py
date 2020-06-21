class Solution:
    def solve(self,n,l):
        k = [0 for _ in range(n)]
        j = 0
        c = 0
        for i in range(n):
            x = l[j] * l[n - i - 1]
            j += 1
            c += x
        return c

    def numTrees(self, n: int) -> int:
            if n==0:
                return 0
            elif n==1:
                return 1
            elif n==2:
                return 2
            elif n==3:
                return 5
            else:
                l = [1, 1, 2, 5]
                for i in range(4, n + 1):
                    x = self.solve(i,l)
                    l.append(x)
                return l[-1]
