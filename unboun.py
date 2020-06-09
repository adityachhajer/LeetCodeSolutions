def solve(nums,W,n):
    if n==1:
        return 1
    else:
        if nums[n-1]>W:
            return solve(nums,W,n-1)
        else:
            return solve(nums,W-nums[n-1],n)+solve(nums,W,n-1)

if __name__ == '__main__':
    nums=[1, 2, 3]
    target=4
    print(solve(nums,target,len(nums)))