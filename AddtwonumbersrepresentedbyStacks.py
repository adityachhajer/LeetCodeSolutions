a=[5, 8, 7, 4]
b=[2, 1, 3]
i=len(a)-1
j=len(b)-1
ans=[]
c=0
d=0
while i>=0 and j>=0:
    ap=a[i]+b[j]+c
    c=ap//10
    d=ap%10
    ans.append(d)
    i-=1
    j-=1
while j>=0:
    ap=b[j]+c
    c=ap//10
    d=ap%10
    ans.append(d)
    j-=1
while i>=0 :
    ap=a[i]+c
    c=ap//10
    d=ap%10
    ans.append(d)
    i-=1

ans=ans[::-1]
print(ans)