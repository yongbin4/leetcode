class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        right: int = len(nums) - 1
        left: int = 0
        operation: int = 0
        while left < right:
            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                operation += 1 
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return operation