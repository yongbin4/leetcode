class Solution(object):
    def coinChange(self, coins, amount):
        # create dp starting with zero
        dp = [0] + [amount + 1] * amount

        # loop from 1 to the amount 
        for i in range(1, amount + 1):
            # for each coin
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != amount + 1 else -1

