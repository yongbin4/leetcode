from typing import List

class Solution:
    def canJump(self,nums):
        if not nums or len(nums) <= 1:
            return True
    
        max_reach = 0  # Maximum index we can reach
        
        for i in range(len(nums)):
            # If current index is beyond our reach, we can't proceed
            if i > max_reach:
                return False
            
            # Update maximum reachable index
            max_reach = max(max_reach, i + nums[i])
            
            # If we can reach the last index, return True
            if max_reach >= len(nums) - 1:
                return True
        
        return False