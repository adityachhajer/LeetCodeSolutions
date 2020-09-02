from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        arr = list(permutations(sorted(A, reverse=True)))
        for a, b, c, d in arr:
            if a * 10 + b < 24 and c * 10 + d < 60:
                return str(a) + str(b) + ':' + str(c) + str(d)
        return ''


