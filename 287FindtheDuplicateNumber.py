class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            if i not in l:
                l.append(i)
            else:
                return i
