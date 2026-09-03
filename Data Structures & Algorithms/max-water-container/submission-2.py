class Solution:
    def maxArea(self, heights: List[int]) -> int:
       left, right = 0, len(heights) - 1
       maxarea = 0

       while left < right:
            currarea = (right - left) * min(heights[left], heights[right])
            if currarea > maxarea:
                maxarea = max(maxarea, currarea)
            
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
       return maxarea
            
            


            



