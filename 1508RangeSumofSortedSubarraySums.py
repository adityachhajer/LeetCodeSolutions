class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        temp = 0
        res = []
        sums = 0
        for i in range(0, n):
            temp = 0
            for j in range(i, n):
                temp += nums[j]
                res.append(temp)
        res.sort()

        return (sum(res[left - 1:right])) % (10 ** 9 + 7)