s = "abc3[cd]xyz"
ans=''
l=[str(i) for i in range(0,9)]
i=0
while i<len(s):
    if s[i] in l:
        x=int(s[i])
        j=i+2
        k=''
        while(s[j]!=']'):
            k=k+s[j]
            j=j+1
        i=j
        ans=ans+ x*k
    else:
        ans=ans+s[i]
    i=i+1
print(ans)