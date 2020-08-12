class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        prev=float('-inf')
        nextt=float('-inf')
        for i in range(1,len(A)):
            prev=max(prev,A[i-1]+i-1)
            nextt=max(nextt,prev+A[i]-i)
        return nextt