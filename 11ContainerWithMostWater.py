class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        l=0
        r=len(height)-1
        while(l<r):
            if height[l]<=height[r]:
                maxarea=max(maxarea,height[l]*(r-l))
                l=l+1
            else:
                maxarea = max(maxarea, height[r] * (r-l))
                r=r-1
        return maxarea