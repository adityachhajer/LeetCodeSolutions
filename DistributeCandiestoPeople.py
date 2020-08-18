class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans=[0 for _ in range(num_people)]
        i=1
        j=0
        data=0
        tot=candies
        while candies>0:
            ans[j]+=i
            candies-=i
            i+=1
            j+=1
            if j==num_people:
                j=0
            data=data+i
            if data>=tot:
                i=candies
        return ans