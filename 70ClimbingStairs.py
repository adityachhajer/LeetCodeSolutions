def solve(n,l):
    if n==0:

        return 1
    if l[n]!=-1:
        return l[n]
    else:
        if n < 2:
            l[n]=solve(n - 1, l)
            return l[n]
        else:
            l[n]=solve(n - 1, l) + solve(n - 2, l)
            return l[n]

if __name__ == '__main__':
    n=int(input())
    l=[-1 for _ in range(n+1)]
    print(solve(n,l))
