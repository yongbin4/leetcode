class Solution(object):
    def trap(self, height):
        # start from the either end
        # when there is a same height each end the it counts any height lower than that

        left = 0
        right = len(height) - 1
        water = 0

        while left < right:
            if height[left] <= height[right]:
                height_point = height[left]
                left += 1
                while height[left] < height_point:
                    water += height_point - height[left]
                    left += 1
            else:
                height_point = height[right]
                right -= 1
                while height[right] < height_point:
                    water += height_point - height[right]
                    right -= 1
        return water