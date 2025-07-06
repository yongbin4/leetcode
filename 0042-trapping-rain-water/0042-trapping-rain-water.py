class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # track highest bar from left and right
        n = len(height)
        left_height, right_height = [0] * n, [0] * n
        for i in range(n):
            if i == 0:
                left_height[i] = height[i]
            else:
                left_height[i] = max(height[i], left_height[i-1])
        
        for i in range(n-1, -1, -1):
            if i == len(height)-1:
                right_height[i] = height[i]
            else:
                right_height[i] = max(height[i], right_height[i+1])
        
        # height =     [0,1,0,2,1,0,1,3,2,1,2,1]
        # left_height= [0,1,1,2,2,2,2,3,3,3,3,3]
        #right_height= [3,3,3,3,3,3,3,3,2,2,2,1]
        #smaller_height[0,1,1,2,2,2,2,3,2,2,2,1]
        smaller_height = []
        for i in range(n):
            smaller_height.append(min(left_height[i], right_height[i]))
        
        result = 0
        for i in range(n):
            result += smaller_height[i] - height[i]
            
        return result
        
        