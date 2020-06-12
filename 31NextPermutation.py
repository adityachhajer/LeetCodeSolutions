class Solution:
    def nextPermutation(self, nums):
        i = len(nums)-1
        while i-1>=0 and nums[i-1]>=nums[i]:
            i -=1
        if i-1>=0:
            j = i
            while j<len(nums) and nums[j]>nums[i-1]:
                j +=1
            nums[i-1],nums[j-1] = nums[j-1],nums[i-1]
        m = i
        n = len(nums)-1
        while m < n:
            nums[m],nums[n] = nums[n],nums[m]
            m +=1
            n -=1