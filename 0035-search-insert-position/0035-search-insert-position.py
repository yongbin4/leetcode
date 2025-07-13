class Solution(object):
    
    def searchInsert(self,nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            pivot = (right + left) // 2  # Use integer division
            
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                right = pivot - 1
        
        # When loop exits, left is the insertion point
        return left
