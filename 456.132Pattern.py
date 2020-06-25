# brute force
# def solve(nums):
#     for i in range(0, len(nums) - 2):
#         for j in range(i + 1, len(nums) - 1):
#             if nums[j]>nums[i]:
#                 for k in range(j + 1, len(nums)):
#                     if nums[k]>nums[i] and nums[k]<nums[j]:
#                         return True
#     return False
#

def solve(nums):
    if len(set(nums))<3:
        return False
    intmin=[nums[0]]
    for i in range(1,len(nums)):
        intmin.append(min(nums[i],intmin[i-1]))
    l=[]
    for i in range(len(nums)-1,-1,-1):
        if nums[i]>intmin[i]:
            while(len(l)!=0 and l[-1]<=intmin[i]):
                l.pop()
            if (len(l)!=0 and l[-1]<nums[i]):
                return True
            l.append(nums[i])
    return False

nums=[3,5,0,3,4]
print(solve(nums))