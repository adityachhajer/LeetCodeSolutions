def solve(s,i,n,x,p):
    if i==n and x==0:
        return True
    if i==n or  x<=0:
        return False
    p=p+s[i]
    if p==p[::-1]:
        return solve(s,i+1,n,x-1,'') or solve(s,i+1,n,x,p)
    else:
        return solve(s,i+1,n,x,p)

if __name__ == '__main__':
    s = 'namananamadammadam'
    print(solve(s,0,len(s),3,''))