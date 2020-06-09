class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minn = float('inf')
        profit = float('-inf')
        for i in range(0, len(prices)):
            minn = min(minn, prices[i])
            if min != prices[i]:
                profit = max(profit, (prices[i] - minn))
        return profit

