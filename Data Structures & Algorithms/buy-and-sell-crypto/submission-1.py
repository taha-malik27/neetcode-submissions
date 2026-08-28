class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        n = len(prices)
        maxP = 0

        while s < n:
            maxP = max(maxP, prices[s] - prices[b])
            if prices[s] < prices[b]:
                b = s
            s += 1

        return maxP
            