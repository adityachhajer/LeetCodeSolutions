# def calculateDiff(i, j, arr):
#     return abs(arr[i] - arr[j]) + abs(i - j)
#
#
# def maxDistance(arr, n):
#     result = 0
#     for i in range(0, n):
#         for j in range(i, n):
#             if (calculateDiff(i, j, arr) > result):
#                 result = calculateDiff(i, j, arr)
#
#     return result
# if __name__ == '__main__':
#     t=int(input())
#     for i in range(0,t):
#         n = int(input())
#         arr = list(map(int, input().split()))[:n]
#         print(maxDistance(arr, n))

#
# #
class sol:
    def find(self,l):
        max1 = float('-inf')
        min1 = float('inf')
        max2 = float('-inf')
        min2 = float('inf')
        for i in range(len(l)):
            max1 = max(max1, l[i] + i)
            min1 = min(min1, l[i] + i)
            max2 = max(max2, l[i] - i)
            min2 = min(min2, l[i] - i)

        return max(max1 - min1, max2 - min2)



if __name__ == '__main__':
    t=int(input())
    for i in range(0,t):
        n = int(input())
        l = list(map(int, input().split()))[:n]
        soll=sol()
        print(soll.find(l))