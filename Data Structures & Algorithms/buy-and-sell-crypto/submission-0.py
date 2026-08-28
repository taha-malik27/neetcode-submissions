class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left and right should never be same right always ahead
        left = 0
        right = 1
        n = len(prices)
        max_profit = 0
        # loop until we reach final sell date possible (end of array)
        while right <= n-1:
            profit = prices[right] - prices[left]
            # calculate and compare profit
            if profit > max_profit:
                max_profit = profit

            # only increment left if right pointer finds cheaper price
            if prices[right] < prices[left]:
                left = right
            
            # always increment right to eventually end loop and also so left != right
            right+=1

        return max_profit