class Solution:
    def maxArea(self, heights: List[int]) -> int:
       left, right = 0, len(heights) - 1
       maxarea = 0

       while left < right:
        if maxarea < (right - left) * min(heights[left], heights[right]):
            maxarea = (right - left) * min(heights[left], heights[right])

        if heights[left] < heights[right]:
            left += 1
        elif heights[right] <= heights[left]:
            right -= 1
        
       return maxarea
