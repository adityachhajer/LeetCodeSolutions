class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums=list(set(nums))
        di={}
        for i in nums:
            di[i]=1
        l=[]
        for i in range(1,n+1):
            if i not in di.keys():
                l.append(i)
        return l