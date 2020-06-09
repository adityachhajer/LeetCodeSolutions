t=int(input())
for _ in range(0,t):
    N=int(input())
    l=list(map(int,input().split()))[:N]
    if N==1:
        print(str(1))
    else:
        # if array contains positive integers-->

        # sumi=0
        # sumj=0
        # i=0
        # j=N-1
        # while(i<j):
        #     if sumi==0 and sumj==0:
        #         sumi+=l[i]
        #         sumj+=l[j]
        #         i+=1
        #         j-=1
        #     else:
        #         if abs(sumi) < abs(sumj):
        #             sumi += l[i]
        #             i += 1
        #         if abs(sumj) < abs(sumi):
        #             sumj += l[j]
        #             j -= 1
        #         if sumi == sumj:
        #             print(i + 1)
        #             break
        # if sumi!=sumj:
        #     print(str(-1))


        # --------------------------------------------


        # if array contains negative too-->

        total=sum(l)
        cursum=0
        i=0
        while(i<len(l)):
            total-=(l[i])
            if total==cursum:
                print(i)
                break
            else:
                cursum+=(l[i])
            i+=1






