class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l = {}
        d = []
        for i in nums:
            if i not in l.keys():
                l[i] = 0
            else:
                d.append(i)
        return d


