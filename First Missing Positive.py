class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums==[]:
            return 1
        di={}
        for i in nums:
            if i>=0 :
                di[i]=1
        if len(di)==0:
            return 1
        n=max(di.keys())
        for i in range(1,n+2):
            if i not in di.keys():
                return i