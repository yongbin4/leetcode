class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # iterate through the nums list
        # using left and right counter to create window

        left = 0
        zero_counter = 0
        longest_ones = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_counter += 1
            
            while zero_counter > k:
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1

            longest_ones = max(longest_ones, right - left + 1)
        
        return longest_ones