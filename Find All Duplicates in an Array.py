class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] >= 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
            else:
                d.append(abs(nums[i]))
        return d

