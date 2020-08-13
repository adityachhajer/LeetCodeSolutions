import math


class Solution:
    def allprime(self, n):
        l = [1 for _ in range(n)]

        for i in range(0, math.ceil(math.sqrt(n))):
            if i == 0 or i == 1:
                l[i] = 0
            if l[i]:
                for j in range(i * i, n, i):
                    l[j] = 0
        return l.count(1)

    def countPrimes(self, n: int) -> int:
        return self.allprime(n)