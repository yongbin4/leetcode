class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return 0

        cliff = nums[0]
        jump = 1
        next_cliff = 0

        for i in range(len(nums)):
            # cliff = 2
            # i = 2
            if i <= cliff:
                # next = 2
                next_cliff = max(next_cliff, nums[i] + i)
            else:
                # jump = 2
                jump += 1
                cliff = next_cliff
                next_cliff = max(next_cliff, nums[i] + i)
            if cliff >= len(nums) - 1:
                return jump

        return jump


        


