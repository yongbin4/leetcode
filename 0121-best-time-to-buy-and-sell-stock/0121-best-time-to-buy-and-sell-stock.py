class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if prices[0] greater than prices[1] update sell
        sell = 0
        buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            sell = prices[i]
            if sell - buy < 0:
                buy = sell
            else:
                max_profit = max(sell - buy, max_profit)
        return max_profit



            

