
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_list = []
        for i in range(len(nums)):
            if nums[i] == val:
                val_list.append(i)
        
        for value in val_list[::-1]:
            nums.pop(value)

        return len(nums)
