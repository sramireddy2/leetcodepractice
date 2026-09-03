class Solution:
    def maxArea(self, heights: List[int]) -> int:
       left, right = 0, len(heights) - 1
       maxarea = 0

       while left < right:
            area = (right - left) * min(heights[left], heights[right])
            if area > maxarea:
                maxarea = area
            else:
                if heights[right] <= heights[left]:
                    right -=1
                else:
                    left += 1

       return maxarea
    

            
            


            



