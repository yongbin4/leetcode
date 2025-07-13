class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        if target <= nums[0]:
            return 0

        while left <= right:
            pivot = (right + left) / 2
            print(pivot)
            if target > nums[pivot]:
                left = pivot + 1
            elif target == nums[pivot]:
                return pivot
            else:
                right = pivot - 1
          
        return pivot if nums[pivot] > target else pivot + 1 
