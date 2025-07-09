class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 0 - 3
        dp = [0] * len(nums)
        if len(nums) == 1: return nums[0]
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
                print(dp)
            elif i == 1:
                if dp[i-1] > nums[i]:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = nums[i]
            else:
                if dp[i-1] > nums[i] + dp[i-2]:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = nums[i] + dp[i-2]
        return dp[-1]

        