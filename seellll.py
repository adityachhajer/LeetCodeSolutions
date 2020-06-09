if __name__ == '__main__':
    n=int(input())
    m=int(input())
    l1=list(map(int,input().split()))[:n]
    l2=list(map(int,input().split()))[:m]
    if len(l1)>len(l2):
        l1=list(set(l1))
        for i in l2:
            if i not in l1:
                l1.append(i)
        print(l1)

