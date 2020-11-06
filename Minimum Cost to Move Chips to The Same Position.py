class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        l=[i%2 for i in position]
        return min(l.count(0),l.count(1))