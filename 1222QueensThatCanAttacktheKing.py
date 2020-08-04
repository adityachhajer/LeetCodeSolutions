class Solution:
    def solveleft(self, l, i, j, n, m):
        while j >= 0:
            if l[i][j] == 0:
                return [i, j]
            j -= 1
        return 0

    def solveright(self, l, i, j, n, m):
        while j < m:
            if l[i][j] == 0:
                return [i, j]
            j += 1
        return 0

    def solveup(self, l, i, j, n, m):
        while i >= 0:
            if l[i][j] == 0:
                return [i, j]
            i -= 1
        return 0

    def solvedown(self, l, i, j, n, m):
        while i < n:
            if l[i][j] == 0:
                return [i, j]
            i += 1
        return 0

    def solveleftup(self, l, i, j, n, m):
        while i >= 0 and j >= 0:
            if l[i][j] == 0:
                return [i, j]
            i -= 1
            j -= 1
        return 0

    def solvedownright(self, l, i, j, n, m):
        while i < n and j < m:
            if l[i][j] == 0:
                return [i, j]
            i += 1
            j += 1
        return 0

    def solveleftdown(self, l, i, j, n, m):
        while i < n and j >= 0:
            if l[i][j] == 0:
                return [i, j]
            i += 1
            j -= 1
        return 0

    def solveupright(self, l, i, j, n, m):
        while i >= 0 and j < m:
            if l[i][j] == 0:
                return [i, j]
            i -= 1
            j += 1
        return 0

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        l = [[-1 for _ in range(8)] for _ in range(8)]
        for i in queens:
            l[i[0]][i[1]] = 0
        l[king[0]][king[1]] = 1
        ans = []
        n = len(l)
        m = len(l[0])
        for i in range(len(l)):
            for j in range(len(l[0])):
                if l[i][j] == 1:
                    a = self.solveleft(l, i, j, n, m)
                    if a != 0:
                        ans.append(a)
                    b = self.solveright(l, i, j, n, m)
                    if b != 0:
                        ans.append(b)
                    c = self.solveup(l, i, j, n, m)
                    if c != 0:
                        ans.append(c)
                    d = self.solvedown(l, i, j, n, m)
                    if d != 0:
                        ans.append(d)
                    e = self.solveleftup(l, i, j, n, m)
                    if e != 0:
                        ans.append(e)
                    f = self.solveleftdown(l, i, j, n, m)
                    if f != 0:
                        ans.append(f)
                    g = self.solveupright(l, i, j, n, m)
                    if g != 0:
                        ans.append(g)
                    h = self.solvedownright(l, i, j, n, m)
                    if h != 0:
                        ans.append(h)
                    return ans

                else:
                    continue