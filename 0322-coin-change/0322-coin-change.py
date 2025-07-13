class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0
        
        # For each amount from 1 to target
        for i in range(1, amount + 1):
            # Try each coin
            for coin in coins:
                # If coin value <= current amount
                if coin <= i:
                    # Update minimum coins needed
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Return result, -1 if impossible
        return dp[amount] if dp[amount] != amount + 1 else -1
