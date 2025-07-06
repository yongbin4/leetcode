class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # [2,3,1,1,4]
        # [T,T,T,T,T]
        
        # [3,2,1,0,4]
        # [T,Tj,i,T,F]
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i, -1, -1):
                if dp[j] == True:
                    gap = i-j
                    if nums[j] >= gap:
                        dp[i] = True
                        break
                else:
                    continue
            if dp[i] == False:
                return False

        return dp[-1]
        
        