from math import *
t=int(input())
for j in range(0,t):
    n = int(input())
    lst = []
    i = 1
    while i * i <= n:
        lst.append(i * i)
        i += 1

    i = 1
    while i < len(lst):
        x = lst[i - 1] + lst[i]
        for d in range(2, int(sqrt(x)) + 1):
            if x % d == 0:
                del lst[i]
                break
        else:
            i += 1

    print(' '.join(map(str, lst)))

