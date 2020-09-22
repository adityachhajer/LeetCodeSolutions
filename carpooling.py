trips = [[5,4,7],[7,4,8],[4,1,8]]
capacity = 17
x=float('-inf')
for i in trips:
    x=max(x,i[2])
ans=[0]*(x+1)

for i in range(len(trips)):
    ans[trips[i][1]]+=trips[i][0]
    ans[trips[i][2]]-=trips[i][0]
c=0
for i in ans:
   c=c+i
   if c>capacity:
       print(False)
       exit()
print(True)