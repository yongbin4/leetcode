class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """

    #     nums1 = self.remove_zero(nums1)
    #     print(nums1)
    #     nums2 = self.remove_zero(nums2)
    #     print(nums2)

    #     for num in nums2:
    #         nums1.append(num)

    #     output = nums1.sort()

    #     return output

    # def remove_zero(self, nums: List[int]) -> List[int]:
    #     for i in range(len(nums) - 1, -1, -1): 
    #         if nums[i] == 0:
    #             nums.pop(i)
    #     return nums

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_end = len(nums1) - 1
        for num in nums2:
            nums1[nums1_end] = num
            nums1_end -= 1
        nums1.sort()