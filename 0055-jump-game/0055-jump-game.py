from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums_length = len(nums)
        stack = [0]
        # store the visited positions
        visited = set()

        # while stack is not empty
        while stack:
            position = stack.pop()

            if position >= nums_length - 1:
                return True
            
            if position not in visited:
                visited.add(position)

            for jump_length in range(1, nums[position] + 1):
                current_position = jump_length + position
                if current_position not in visited:
                    stack.append(current_position)

        return False