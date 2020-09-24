class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        startindex=0
        fuel=0
        for i in range(len(gas)):
            if gas[i] + fuel<cost[i]:
                startindex=i+1
                fuel=0
            else:
                fuel+=(gas[i]-cost[i])
        return startindex