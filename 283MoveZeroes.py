class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                c = c + 1
        for i in range(0, c):
            nums.remove(0)
            nums.append(0)
        """
        Do not return anything, modify nums in-place instead.
        """
