def solve(a,n):
    ans=[]*n
    stack=[]
    i=n-1
    while i>=0:
        if len(stack)==0 or stack[-1]>a[i]:
            stack.append(a[i])
            ans.append(len(stack)-1)
        else:
            while stack and stack[-1]<=a[i]:
                stack.pop(-1)
            stack.append(a[i])
            ans.append(len(stack) - 1)
        i-=1
    ans.reverse()
    return ans


A = [1, 2, 3, 5, 4]
N = 5
print(solve(A,N))