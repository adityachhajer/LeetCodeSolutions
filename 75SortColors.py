class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c1 = 0
        c2 = 0
        c3 = 0
        for i in nums:
            if i == 0:
                c1 += 1
            elif i == 1:
                c2 += 1
            else:
                c3 += 1
        for i in range(len(nums)):
            if c1 != 0:
                nums[i] = 0
                c1 -= 1
            elif c2 != 0:
                nums[i] = 1
                c2 -= 1
            else:
                nums[i] = 2
        return nums
