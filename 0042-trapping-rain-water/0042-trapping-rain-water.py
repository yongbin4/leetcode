# class Solution:
#     def trap(self, height: List[int]) -> int:
#         boundary = self.boundary(height)
#         print(boundary)
#         min_height = 0
#         water = 0
#         for i in range(0,len(boundary), 2):
#             min_height = min(height[boundary[i]],height[boundary[i+1]])
#             for j in range(boundary[i], boundary[i+1]):
#                 if j == 0:
#                     pass
#                 else:
#                     water += height[boundary[i]] - height[j]
#         return water

#     def boundary(self, height: List[int]) -> List[int]:
#         boundary = []
#         i = 0
#         while i < len(height) - 1:
#             for j in range(i+1,len(height)):
#                 if height[i] > height[j]:
#                     if j == len(height) - 1:
#                         i += 1
#                     else:
#                         pass
#                 else:
#                     if i == 0 and height[i] == 0:
#                         i = j
#                         break
#                     else:
#                         pass
#                     boundary.append(i)
#                     i = j
#                     boundary.append(j)
#                     break    
#         return boundary   

# if the first block and the last block is the same size the next bllck that is less must create water
# 

class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        water = 0
        
        while start < end:
            if height[start] <= height[end]:
                current_height = height[start]
                start += 1
                while start < end and height[start] < current_height:
                    water += current_height - height[start]
                    start += 1
            else:
                current_height = height[end]
                end -= 1
                while start < end and height[end] < current_height:
                    water += current_height - height[end]
                    end -= 1
        return water

            
                
