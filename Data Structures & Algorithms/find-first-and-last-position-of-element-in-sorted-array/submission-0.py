class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def binarysearch(target):
            left, right = 0, n
            while left < right:
                mid = (left + (right - 1)) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        start = binarysearch(target)

        if start == n or nums[start] != target:
            return [-1, -1]

        return [start, binarysearch(target + 1) - 1]
        

        