def solve(l,n):
    if n<=0:
        return 0
    if n==1:
        return l[n-1]
    else:
        return max(l[n-1]+solve(l,n-2),solve(l,n-1))

if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        N=int(input())
        l=list(map(int,input().split()))[:N]
        print(solve(l,N))
