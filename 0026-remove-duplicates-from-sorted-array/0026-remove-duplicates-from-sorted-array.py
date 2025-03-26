class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        for num in nums:
            if num not in new_list:
                new_list.append(num)

        nums[:] = new_list  # Modify nums in-place using slicing
        return len(nums)