class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        
        for i in range(1, n):
            for j in range(i-1, -1, -1):  # Start from i-1, not i
                if dp[j] and nums[j] >= (i - j):
                    dp[i] = True
                    break
        
        return dp[-1]  # Only check the last position