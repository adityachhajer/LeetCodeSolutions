from itertools import *
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l=[]
        x=list(permutations(nums,len(nums)))
        for i in x:
            i=list(i)
            if i not in l:
                l.append(i)
        return l