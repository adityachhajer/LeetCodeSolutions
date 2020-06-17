class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        t = 0
        i = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c = c + 1
            else:
                t = max(t, c)
                c = 0
        return max(t, c)

