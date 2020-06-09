class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = list(nums)
        for i in l:
            if i == val:
                nums.remove(val)
        return len(nums)

