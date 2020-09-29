class Solution:
    def solve(self, i):
        if i == 0:
            return 0
        if i == 1:
            return 1
        c = 1
        for j in range(2, i + 1):
            c = c + j
        return c
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p = 1
        l = []
        ans = 0
        for i in nums:
            p = p * i
            if p < k:
                l.append(i)
            else:
                while l and p >= k:
                    ans += len(l)
                    x = l.pop(0)
                    p = p / x
                if len(l) == 0:
                    p = i
                if p < k:
                    l.append(i)
                else:
                    p = 1
        a = self.solve(len(l))
        return ans + a