class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # [2,3,1,1,4]
        # [T,T,T,T,T]
        # [2,3,1,1,4]
        # [0,1,2,3,4]
        
        # [3,2,1,0,4]
        # [T,Tj,i,T,F]
        if len(nums) == 0 or len(nums) == 1:
            return True
        
        max_current = 0
        for i in range(len(nums)):
            if i > max_current:
                return False
            max_current = max(max_current, nums[i] + i)
            if max_current >= len(nums) - 1:
                return True
        return False
            
        
        # n = len(nums)
        # dp = [False] * n
        # dp[0] = True
        # for i in range(1, n):
        #     for j in range(i, -1, -1):
        #         if dp[j] == True:
        #             gap = i-j
        #             if nums[j] >= gap:
        #                 dp[i] = True
        #                 break
        #     if dp[i] == False:
        #         return False

        # return dp[-1]
