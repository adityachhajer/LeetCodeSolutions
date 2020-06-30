def solve(nums,i):
    if i==len(nums)-1:
        return True
    elif i>=len(nums):
        return False
    else:
        x = nums[i]
        if x==0:
            return False
        c=False
        for j in range(1,x+1):
            c = c or solve(nums,i+j)
        return c


nums =[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8]
if nums==[]:
    print(True)
else:
    print(solve(nums,0))