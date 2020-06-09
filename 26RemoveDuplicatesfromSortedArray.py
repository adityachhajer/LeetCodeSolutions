class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        index = 0
        temp = nums[0]

        for j in range(1, len(nums)):
            if temp == nums[j]:
                continue
            else:
                index += 1
                nums[index] = nums[j]
                temp = nums[j]

        return index + 1