class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        l1 = []
        l2 = []
        for i in S:
            if i != '#':
                l1.append(i)
            else:
                if len(l1) > 0:
                    l1.pop(-1)
        for i in T:
            if i != '#':
                l2.append(i)
            else:
                if len(l2) > 0:
                    l2.pop(-1)
        if (l1 == l2):
            return True
        else:
            return False

