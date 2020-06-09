class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        x = sorted(nums)
        ii = 0
        jj = 0
        for i in range(0, len(nums)):
            if nums[i] != x[i]:
                ii = i
                break
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] != x[j]:
                jj = j
                break
        if ii == 0 and jj == 0:
            return 0
        else:
            return (jj - ii + 1)


