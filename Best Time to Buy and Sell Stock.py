class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        p = list(prices)
        p.sort(reverse=True)
        if (p == prices): return 0

        minn = float('inf')
        profit = float('-inf')
        for i in range(len(prices)):
            minn = min(minn, prices[i])
            if minn != prices[i]:
                profit = max(profit, prices[i] - minn)
        return profit