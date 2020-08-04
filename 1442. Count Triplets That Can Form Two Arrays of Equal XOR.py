class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        a=0
        for i in range(0,len(arr)):
            xorr=0
            for j in range(i,len(arr)):
                xorr^=arr[j]
                b=0
                for k in range(j+1,len(arr)):
                    b^=arr[k]
                    if xorr==b:
                        a+=1
        return a