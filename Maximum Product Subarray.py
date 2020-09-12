class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=nums
        curmin=a[0]
        curmax=a[0]
        prevmin=a[0]
        prevmax=a[0]
        result=a[0]
        for i in range(1,len(a)):
            curmax=max(a[i],prevmax*a[i],prevmin*a[i])
            curmin=min(a[i],prevmax*a[i],prevmin*a[i])
            result=max(result,curmax)
            prevmax=curmax
            prevmin=curmin
        return (result)