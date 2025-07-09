class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*n
        for i in range(n):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 2
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
