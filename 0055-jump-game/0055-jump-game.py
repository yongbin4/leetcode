from typing import List

class Solution:
    def canJump(self, nums):
        max_current = 0
        
        if len(nums) == 0 or len(nums) == 1:
            return True

        for position in range(len(nums)):

            if position > max_current:
                return False

            max_current = max(max_current, position + nums[position])
            if max_current >= len(nums) - 1:
                return True
        
        return False
        