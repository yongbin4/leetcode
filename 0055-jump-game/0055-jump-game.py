from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = [0]  # Start at index 0
        visited = set()

        while stack:
            position = stack.pop()

            if position >= n - 1:
                return True  # Reached the end

            if position in visited:
                continue

            visited.add(position)

            # Try all possible jumps from this position
            for jump_length in range(1, nums[position] + 1):
                next_position = position + jump_length
                if next_position not in visited:
                    stack.append(next_position)

        return False  # Tried all paths, can't reach the end
