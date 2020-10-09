class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            a=(i+j)//2
            if nums[a]==target:
                return a
            elif nums[a]<target:
                i=a+1
            else:
                j=a-1
        return -1